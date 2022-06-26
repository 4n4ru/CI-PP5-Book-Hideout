from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.contrib import messages

from book_hideout.mixins import SuperUserMixin
from .models import Sale
from .forms import SaleForm


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


class AddSale(SuperUserMixin, View):
    form = SaleForm()
    template = 'sale/add_sale.html'
    context = {
        'form': form,
    }

    def get(self, request):
        """Renders add sale form

        Args:
            request (object): HTTP request object

        Returns:
            method: renders add sale form
        """
        return render(request, self.template, self.context)
    
    def post(self, request):
        """Handles post method of add sale form

        Args:
            request (object): HTTP request object

        Returns:
            method: redirects back to add manage sales page
        """
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            sale = form.save()
            messages.success(request, 'The sale was successfully added')
            return redirect(reverse('manage'))
        else:
            messages.error(
                request,
                'Failed to add sale. Please ensure the form is valid'
            )
            return render(request, self.template, {'form': form})


class DeleteSale(SuperUserMixin, View):
    """A view to delete sale from database

    Args:
        View (class): Built in parent class for views
    """

    def get(self, request, sale_id):
        """Deletes sale from database 

        Args:
            request (object): HTTP request object

        Returns:
            method: redirects to manage sales page
        """
        sale = get_object_or_404(Sale, pk=sale_id)
        sale.delete()
        messages.success(
            request,
            f'You deleted {sale.name}'
        )
        return redirect(reverse('manage'))