from django.shortcuts import render
import requests
from django.conf import settings

# Homepage view
def homepage(request):
    restaurant_name = getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    try:
        response = requests.get('http://localhost:8000/api/products/menu/') #API Endpoint
        response.raise_for_status() # Raise error if API fails
        menu_items = response.json()
    except requests.RequestException:
        menu_items = []

    return render(request, 'menu.html', {
            'menu_items':menu_items,
            'restaurant_name':restaurant_name,
        })
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