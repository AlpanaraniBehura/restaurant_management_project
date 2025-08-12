from django.shortcuts import render
import requests
from django.conf import settings

# Homepage view
def homepage(request):
    restaurant_name = getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    image_url="https//picsum.photos/800/300?"
    return render(request, 'menu.html', {
            'restaurant_name':restaurant_name,
            'image_url':image_url
        })
# Hardcoded Menu List View
def menu_list(request):
    restaurant_name="Our Restaurant"
# Temporary hardcoded menu items
manu_
# About page view
def about(request):
    restaurant_name=getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    image_url = "https://picsum.photos/800/300?random=2" # Random Placeholder image 
    
    return render(request, 'about.html',{
        'restaurant_name':restaurant_name,
        'description':"We are a family-run restaurant serving fresh,delicious meals made from locally sourced ingredients",
        'image_url':image_url
    })
#Custom 404 page view
def custom_404(request, exception):
    return render(request, '404.html', status=404) 