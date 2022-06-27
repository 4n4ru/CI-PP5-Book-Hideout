# Imports:
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib import messages
from django.db.models import Q
from datetime import date

# Internal:
from .models import Product, Genre
from .forms import ProductForm
from book_hideout.mixins import SuperUserMixin
from sale.models import Sale


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
        products_query = Product.objects.all()
        sales = Sale.objects.filter(
            Q(start_date__lte=date.today())
            & Q(end_date__gte=date.today())
        )

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

            products_query = products_query.filter(queries)

        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            products_query = products_query.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

        products = list(products_query)

        if sales:
            sale = sales.first()
            for product in products:
                product.on_sale = False
            for book in sale.books.all():
                for product in products:
                    if product.id == book.id:
                        product.old_price = product.price
                        product.on_sale = True
                        print(product)
                        product.price = self.sale_price(
                            sale.percentage,
                            product.price
                        )

        query = None
        genres = None
        sort = None
        direction = None

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            desc = False
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    desc = True

            if sortkey == 'title':
                products.sort(key=self.get_title, reverse=desc)

            if sortkey == 'authors':
                products.sort(key=self.get_authors, reverse=reverse)

            if sortkey == 'price':
                products.sort(key=self.get_price, reverse=reverse)

            if sortkey == 'rating':
                products.sort(key=self.get_rating, reverse=reverse)

        if 'sale' in request.GET:
            if sales:
                products = [p for p in products if p.on_sale]
            else:
                products = []

        current_sorting = f'{sort}_{direction}'

        context = {
            'products': products,
            'search_term': query,
            'current_genres': genres,
            'current_sorting': current_sorting,
        }

        return render(request, 'products/products.html', context)

    def sale_price(self, percentage, price):
        return round(price * (100 - percentage) / 100, 2)

    def get_price(self, product):
        return product.price

    def get_authors(self, product):
        return product.authors.lower()

    def get_title(self, product):
        return product.title.lower()

    def get_rating(self, product):
        return product.rating


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
        sales = Sale.objects.filter(
            Q(start_date__lte=date.today())
            & Q(end_date__gte=date.today())
        )

        if sales:
            sale = sales.first()
            for book in sale.books.all():
                if product.id == book.id:
                    product.old_price = product.price
                    product.price = self.sale_price(
                        sale.percentage,
                        product.price
                    )

        context = {
            'product': product,
        }

        return render(request, 'products/product_details.html', context)

    def sale_price(self, percentage, price):
        return round(price * (100 - percentage) / 100, 2)


class AddProduct(SuperUserMixin, View):
    """A view to display add product template and add products to database

    Args:
        View (class): Built in parent class for views
    """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    def get(self, request):
        """Renders add product form

        Args:
            request (object): HTTP request object

        Returns:
            method: renders add product form
        """
        return render(request, self.template, self.context)

    def post(self, request):
        """Handles post method of add product form

        Args:
            request (object): HTTP request object

        Returns:
            method: redirects back to add product page
        """
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'The book was successfully added')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid'
            )
            return render(request, self.template, {'form': form})


class EditProduct(SuperUserMixin, View):
    """A view to display edit product template and edit products in database

    Args:
        View (class): Built in parent class for views
    """
    template = 'products/edit_product.html'

    def get(self, request, product_id):
        """Renders edit product form

        Args:
            request (object): HTTP request object

        Returns:
            method: renders edit product form
        """
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(instance=product)
        messages.info(
            request,
            f'You are editing the book {product.title} by {product.authors}'
        )
        context = {
            'form': form,
            'product': product,
        }
        return render(request, self.template, context)

    def post(self, request, product_id):
        """Handles post method of edit product form

        Args:
            request (object): HTTP request object

        Returns:
            method: redirects back to product page
        """
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        context = {
            'form': form,
            'product': product,
        }
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'The book {product.title} by \
                    {product.authors} was successfully updated'
            )
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update book. Please ensure the form is valid'
            )
            return render(request, self.template, context)


class DeleteProduct(SuperUserMixin, View):
    """A view to delete products from database

    Args:
        View (class): Built in parent class for views
    """

    def get(self, request, product_id):
        """Deletes product from database

        Args:
            request (object): HTTP request object

        Returns:
            method: redirects to product page
        """
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(
            request,
            f'You deleted {product.title} by {product.authors}'
        )
        return redirect(reverse('products'))
