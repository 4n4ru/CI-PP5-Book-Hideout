from django.urls import path
from . import views

urlpatterns = [
    path(
        'manage',
        views.AllSales.as_view(),
        name='manage'
    ),
    path(
        'add',
        views.AddSale.as_view(),
        name='add_sale'
    ),
    path(
        'delete/<int:sale_id>/',
        views.DeleteSale.as_view(),
        name='delete_sale'
    ),
    path(
        'edit/<int:sale_id>/',
        views.EditSale.as_view(),
        name='edit_sale'
    ),
]
