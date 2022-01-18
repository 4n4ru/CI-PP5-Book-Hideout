from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts.as_view(), name='products'),
    path('<product_id>', views.ProductDetails.as_view(), name='product_details'),
]
