# Imports:
# 3rd party:
from django.shortcuts import render, redirect, reverse, HttpResponse,\
    get_object_or_404
from django.views import View
from django.contrib import messages

# Internal:
from products.models import Product


class Bag(View):
    """A view to display the shopping bag page

    Args:
        View (class): Built in parent class for views
    """
    def get(self, request):
        """Renders the shopping bag page

        Args:
            request (object): HTTP request object

        Returns:
            method: renders shopping bag page
        """
        return render(request, 'bag/bag.html')


class AddToBag(View):
    """Adding items to bag

    Args:
        View (class): Built in parent class for views
    """
    def post(self, request, item_id):
        """Adding items to bag

        Args:
            request (object): HTTP request object
            item_id (int): id of product being added to the bag

        Returns:
            method: redirects back to the redirect_url passed into the form
        """
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.title} by {product.authors} '
                f'quantity to {bag[item_id]}'
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request,
                f'{product.title} by {product.authors} '
                'was added to your basket.'
            )

        request.session['bag'] = bag
        return redirect(redirect_url)


class AdjustBag(View):
    """Adjusting the quantity of specific item in bag

    Args:
        View (class): Built in parent class for views
    """
    def post(self, request, item_id):
        """Adjusting quantity of specific item in bag,
        if the quantity is set to 0 remove the item

        Args:
            request (object): HTTP request object
            item_id (int): id of product being adjusted

        Returns:
            method: redirects back to the bag
        """
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.title} by {product.authors} '
                f'quantity to {bag[item_id]}'
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                f'{product.title} by {product.authors} '
                'was removed from your basket.'
            )

        request.session['bag'] = bag
        return redirect(reverse('bag'))


class RemoveFromBag(View):
    """Remove the specific item from the bag

    Args:
        View (class): Built in parent class for views
    """
    def post(self, request, item_id):
        """Remove the specific item from the bag

        Args:
            request (object): HTTP request object
            item_id (int): id of product being removed

        Returns:
            method: redirects back to the bag
        """
        try:
            product = get_object_or_404(Product, pk=item_id)
            bag = request.session.get('bag', {})
            bag.pop(item_id)
            messages.success(
                request,
                f'{product.title} by {product.authors} '
                'was removed from your basket.'
            )
            request.session['bag'] = bag
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)
