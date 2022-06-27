# Imports:
# 3rd party:
from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.db.models import Q
from datetime import date

# Internal:
from products.models import Product
from sale.models import Sale


def bag_contents(request):
    """Context processor for the bag content

    Args:
        request (object): HTTP request object

    Returns:
        dictionary: context
    """
    bag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        sales = Sale.objects.filter(
            Q(start_date__lte=date.today())
            & Q(end_date__gte=date.today())
        )

        if sales:
            sale = sales.first()
            for book in sale.books.all():
                if product.id == book.id:
                    product.price = sale_price(sale.percentage, product.price)

        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = Decimal(delivery) + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context


def sale_price(percentage, price):
    return round(price * (100 - percentage) / 100, 2)
