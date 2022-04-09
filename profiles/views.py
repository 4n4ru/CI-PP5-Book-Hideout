# Imports:
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.views import View

# Internal:
from .models import UserProfile
from .forms import USerProfileForm


class Profile(View):
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

        form = USerProfileForm(instance=profile)
        orders = profile.orders.all()

        template = 'profiles/profile.html'
        context = {
            'form': form,
            'orders': orders,
        }

        return render(request, template, context)
