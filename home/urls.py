from django.urls import path
from home.views import homepage, about

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/',views.about, name='about'),
    path('menu-list/', views.menu-list, name='menu-list'),
    
]