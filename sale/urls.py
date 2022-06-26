from django.urls import path
from . import views

urlpatterns = [
    path(
        'manage_sales',
        views.AllSales.as_view(),
        name='sales'
    ),
]
