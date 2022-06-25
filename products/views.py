# Imports:
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Internal:
from .models import Product, Genre
from .forms import ProductForm


class SuperUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    """A Mixin for checking if a logged in user is a superuser and
    handling no permission error. If the user is not a superuser they are
    redirected to the home page and a info message is displayed. If the user is
    a superuser, the view is executed normally

    Args:
        LoginRequiredMixin (class): A mixin that redirects a user who isn't
        logged in to the settings.LOGIN_URL. If the user is logged in, execute
        the view normally.
        UserPassesTestMixin (class): A mixin that limits the access based on
        certain permission or test
    """

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.info(self.request, 'Ooops! Only an Admin can to that!')
        return redirect(reverse('home'))


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
        sort = None
        direction = None

        if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'title':
                    sortkey = 'lower_title'
                    products = products.annotate(lower_title=Lower('title'))

                if sortkey == 'author':
                    sortkey = 'lower_authors'
                    products = products.annotate(
                        lower_authors=Lower('authors')
                    )

                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

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

        current_sorting = f'{sort}_{direction}'

        context = {
            'products': products,
            'search_term': query,
            'current_genres': genres,
            'current_sorting': current_sorting,
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
            return render(request, self.template, {'form': form})


class DeleteProduct(SuperUserMixin, View):
    """A view to delete products from database

    Args:
        View (class): Built in parent class for views
    """

    def get(self, request, product_id):
        """Renders delete product form

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
