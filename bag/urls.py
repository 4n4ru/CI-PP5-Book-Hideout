from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bag.as_view(), name='bag'),
]
