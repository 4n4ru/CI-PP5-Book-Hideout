from django.shortcuts import render
from django.views import View


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

        template = 'profiles/profile.html'
        context = {}

        return render(request, template, context)
