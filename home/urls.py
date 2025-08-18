from django.urls import path
from home.views import homepage, about, contact_us

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/',views.about, name='about'),
    path('menu-list/', views.menu-list, name='menu-list'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('reservations/'views.reservations, name='reservatiuons'),
    
]