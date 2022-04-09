# Imports:
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.views import View

# Internal:
from .models import UserProfile


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
        template = 'profiles/profile.html'
        context = {
            'profile': profile,
        }

        return render(request, template, context)
