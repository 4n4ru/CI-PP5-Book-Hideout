from django.shortcuts import render
from django.views import View


class Home(View):
    """A view to display the home page

    Args:
        View (class): Built in parent class for views
    """
    def get(self, request):
        """Renders the home page

        Args:
            request (object): HTTP request object

        Returns:
            method: renders home page
        """
        return render(request, 'home/index.html')
