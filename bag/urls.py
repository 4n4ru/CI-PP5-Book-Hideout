from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bag.as_view(), name='bag'),
    path('add/<item_id>/', views.AddToBag.as_view(), name='add_to_bag'),
    path('adjust/<item_id>/', views.AdjustBag.as_view(), name='adjust_bag'),
    path(
        'remove/<item_id>/',
        views.RemoveFromBag.as_view(),
        name='remove_from_bag'
    ),
]
