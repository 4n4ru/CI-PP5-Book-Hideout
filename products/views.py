# Imports:
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib import messages
from django.db.models import Q

# Internal:
from .models import Product, Genre


class AllProducts(View):
    """A view to display the products page, including sorting and search queries

    Args:
        View (class): Built in parent class for views
    """
    def get(self, request):
        """Renders the products page

        Args:
            request (object): HTTP request object

        Returns:
            method: renders products page
        """

        products = Product.objects.all()
        query = None
        genres = None

        if request.GET:
            if 'genre' in request.GET:
                genres = request.GET['genre'].split(',')
                products = products.filter(genre__name__in=genres)
                genres = Genre.objects.filter(name__in=genres)


            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(
                        request,
                        "You didn't enter any search criteria!"
                    )
                    return redirect(reverse('products'))

                queries = (
                    Q(title__icontains=query)
                    | Q(authors__icontains=query)
                    | Q(isbn__icontains=query)
                    | Q(isbn13__icontains=query)
                )

                products = products.filter(queries)

        context = {
            'products': products,
            'search_term': query,
            'current_genres': genres,
        }

        return render(request, 'products/products.html', context)


class ProductDetails(View):
    """A view to display the individual product details

    Args:
        View (class): Built in parent class for views
    """
    def get(self, request, product_id):
        """Renders the product details page

        Args:
            request (object): HTTP request object

        Returns:
            method: renders products detail page
        """

        product = get_object_or_404(Product, pk=product_id)

        context = {
            'product': product,
        }

        return render(request, 'products/product_details.html', context)
