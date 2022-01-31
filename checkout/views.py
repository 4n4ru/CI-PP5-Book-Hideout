# Imports:
# 3rd party:
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.conf import settings

import stripe

# Internal:
from bag.contexts import bag_contents
from products.models import Product
from .models import OrderLineItem, Order
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
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request,
                "There's nothing in your bag at the moment"
            )
            return redirect(reverse('products'))
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        order_form = OrderForm()
        if not stripe_public_key:
            messages.warning(
                request,
                'Stripe public key is missing. \
                Did you forget to set it in your environment?'
            )

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


    def post(self, request):
        """Handle the checkout form post request,
        if the form was valid render the
        checkout_success view, if there is an item in the page
        that doesn't exist return to the bag page.

        Args:
            request (object): HTTP request object

        Returns:
            method: render checkout_success page
        """
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id in bag.items():
                try:
                    product = Product.objects.get(id=item_id[0])
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_id[1],
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        "One of the products in your basket wasn't found\
                        in our database. Please call us for assistance!"
                    )
                    order.delete()
                    return redirect(reverse('bag'))
            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse(
                'checkout_success',
                args = [order.order_number]
            ))
        else:
            messages.error(
                request,
                'There was an error with your form.\
                Please double check your information.'
            )


class CheckoutSuccess(View):
    """A view to display the checkout success page

    Args:
        View (class): Built in parent class for views
    """
    def get (self, request, order_number):
        """
        Handle successful checkouts
        """
        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number=order_number)
        messages.success(
            request,
            f'Order successfully processed! \
            Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.'
        )

        if 'bag' in request.session:
            del request.session['bag']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
        }

        return render(request, template, context)
