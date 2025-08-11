from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.
def homepage(request):
    restaurant_name = getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    try:
        response = requests.get('http://localhost:8000/api/products/menu/') # API Endpoint
        response.raise_for_status() # Raise a error if API fails
        menu_items = response.json()
    except requests.RequestException:
        menu_items = []
        return render(request, 'menu.html', {'menu_items': menu_items, 'restaurant_name':restaurant_name})

def custom_404(request, exception):
    return render(request, '404.html', status=404)
