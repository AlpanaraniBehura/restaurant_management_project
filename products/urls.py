from django.urls import path
from .views import *
from .views import MenuAPIView, ItemView

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path(),
    path(),
]