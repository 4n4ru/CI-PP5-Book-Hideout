# Imports:
# 3rd party:
from django.urls import path

# Internal:
from . import views

urlpatterns = [
    path('', views.Profile.as_view(), name='profile'),
    path(
        'order_history/<order_number>',
        views.OrderHistory.as_view(),
        name='order_history'
    ),
]
