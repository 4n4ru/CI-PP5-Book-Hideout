# Imports:
# 3rd party:
from django.shortcuts import render, redirect
from django.views import View

# Internal:

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
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

        request.session['bag'] = bag
        return redirect(redirect_url)
