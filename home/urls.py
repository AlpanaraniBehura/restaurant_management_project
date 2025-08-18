from django.urls import path
import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/',views.about, name='about'),
    path('menu-list/', views.menu-list, name='menu-list'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('reservations/', views.reservations, name='reservations'),
    
]