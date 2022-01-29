# Imports:
# 3rd party:
from django.shortcuts import render , reverse, redirect
from django.views import View
from django.contrib import messages

# Internal:
from .forms import OrderForm

class Checkout(View):
    """A view to display the checkout page

    Args:
        View (class): Built in parent class for views
    """
    def get(self, request):
        """Renders the checkout page

        Args:
            request (object): HTTP request object

        Returns:
            method: renders checkout page
        """        
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request,
                "There's nothing in your bag at the moment"
            )
            return redirect(reverse('products'))
        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
        }
        return render(request, template, context)
