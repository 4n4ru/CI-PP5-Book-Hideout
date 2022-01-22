# Imports:
# 3rd party:
from django.shortcuts import render
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
