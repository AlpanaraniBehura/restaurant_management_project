from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

# Homepage view
def homepage(request):
    restaurant_name = getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    phone_number = getattr(settings,"RESTAURANT_PHONE", "Not Available")
    image_url="https://picsum.photos/800/300?"
    return render(request, 'menu.html', {
            'restaurant_name':restaurant_name,
            'phone_number':phone_number,
            'image_url':image_url
            
    })
# Hardcoded Menu List View
def menu_list(request):
    restaurant_name="Our Restaurant"
    # Temporary hardcoded menu items
    try:
        menu_items= [
            {
                "name":"Margherita Pizza",
   
                "price":250,
                "description":"Classic cheese and tomato pizza."
            },
            {
                "name":"Paneer Butter Masala",
                "price":400,
                "description":"Creamy tomato gravy with soft paneer cubes."
            },
            {
                "name":"Veg Biriyani",
                "price":200,
                "description":"Fragrant rice cooked with vegetables and spices."
            },
            {
                "name":"Chocolate Brownie",
                "price":150,
                "description":"Rich chocolate brownie with ice cream."
            },
        ]
        
        return render(request, "menu_list.html",{
            "restaurant_name":restaurant_name,
            "menu_items":menu_items
        })
    except Exception as e:
        return HttpResponse(f"Something went wrong while loading the menu: {str(e)}, status=500")
# About page view
def about(request):
    restaurant_name=getattr(settings, "RESTAURANT_NAME", "Our Restaurant")
    phone_number=getattr(settings, "RESTAURANT_PHONE", "Not Available")
    image_url = "https://picsum.photos/800/300?random=2" # Random Placeholder image 
    
    return render(request, 'about.html',{
        'restaurant_name':restaurant_name,
        'phone_number':phone_number,
        'description':"We are a family-run restaurant serving fresh,delicious meals made from locally sourced ingredients",
        'image_url':image_url
    })
# Contact us page view
def contact_us(request):
    return render(request, 'contact_us.html')
#Custom 404 page view
def custom_404(request, exception):
    return render(request, '404.html', status=404) 