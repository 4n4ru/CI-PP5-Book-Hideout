# Imports:
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Internal:
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


class Profile(LoginRequiredMixin, View):
    """A view to display the profile page

    Args:
        View (class): Built in parent class for views
    """
    def get(self, request):
        """Renders the profile page

        Args:
            request (object): HTTP request object

        Returns:
            method: renders profile page
        """
        profile = get_object_or_404(UserProfile, user=request.user)

        form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

        template = 'profiles/profile.html'
        context = {
            'form': form,
            'orders': orders,
            'on_profile_page': True
        }

        return render(request, template, context)

    def post(self, request):
        """Handles the post method from the user profile form

        Args:
            request (object): HTTP request object

        Returns:
            method: redirects back to profile page
        """
        profile = get_object_or_404(UserProfile, user=request.user)
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

        return redirect('profile')


class OrderHistory(View):
    """A view to display the order history page

    Args:
        View (class): Built in parent class for views
    """
    def get(self, request, order_number):
        """Renders the order history page

        Args:
            request (object): HTTP request object
            order_number (string): order number

        Returns:
            method: renders order history page
        """
        order = get_object_or_404(Order, order_number=order_number)

        messages.info(
            request,
            f'This is a past confirmation for order number {order_number}. \
            A confirmation email was sent on the order date.'
        )
        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'from_profile': True,
        }

        return render(request, template, context)
