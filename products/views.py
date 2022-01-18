# Imports:
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.views import View

# Internal:
from .models import Product


class AllProducts(View):
    """A view to display the products page, including sorting and search queries

    Args:
        View (class): Built in parent class for views
    """
    def get(self, request):
        """Renders the products page

        Args:
            request (object): HTTP request object

        Returns:
            method: renders products page
        """

        products = Product.objects.all()

        context = {
            'products': products,
        }

        return render(request, 'products/products.html', context)


class ProductDetails(View):
    """A view to display the individual product details

    Args:
        View (class): Built in parent class for views
    """
    def get(self, request, product_id):
        """Renders the product details page

        Args:
            request (object): HTTP request object

        Returns:
            method: renders products detail page
        """

        product = get_object_or_404(Product, pk=product_id)
        
        context = {
            'product': product,
        }

        return render(request, 'products/product_details.html', context)
