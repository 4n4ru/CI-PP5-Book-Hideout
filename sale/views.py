from django.shortcuts import render
from django.views import View


from book_hideout.mixins import SuperUserMixin
from .models import Sale


class AllSales(SuperUserMixin, View):
    def get(self, request):
        """Renders the manage sales page

        Args:
            request (object): HTTP request object

        Returns:
            method: renders manage sales page
        """
        sales = Sale.objects.all()

        context = {
            'sales': sales,
        }

        return render(request, 'sale/manage_sales.html', context)
