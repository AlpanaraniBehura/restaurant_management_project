from django.urls import path
from .views import *
from .views import MenuAPIView, ItemView

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/', MenuAPIView.as_view(), name='static-menu'),
    path('items/', ItemView.as_view(), name='item-list-create'),
]