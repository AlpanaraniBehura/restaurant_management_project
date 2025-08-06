from django.shortcuts import render
import requests

# Create your views here.
def homepage(request):
    response = request.get('http://localhost:8000/api/products/menu/') # API Endpoint
    menu_items = response.json()
    return render(request, 'menu.html', {'menu_items': menu_items})
