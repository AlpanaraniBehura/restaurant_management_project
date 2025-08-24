from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/',views.about, name='about'),
    path('menu_list/', views.menu_list, name='menu_list'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('reservations/', views.reservations, name='reservations'),
    path('feedback/', views.feedback_view, name='feedback'),
    
]