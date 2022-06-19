from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.AllProducts.as_view(),
        name='products'
    ),
    path(
        '<int:product_id>/',
        views.ProductDetails.as_view(),
        name='product_details'
    ),
    path(
        'add/',
        views.AddProduct.as_view(),
        name='add_product'
    ),
    path(
        'edit/<int:product_id>/',
        views.EditProduct.as_view(),
        name='edit_product'
    ),
    path(
        'delete/<int:product_id>/',
        views.DeleteProduct.as_view(),
        name='delete_product'
    ),
    
]
