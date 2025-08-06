from django.urls import path
from .views import *
from .views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    
]