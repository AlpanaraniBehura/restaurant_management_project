from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from .forms import FeedbackForm
from .models import MenuItem

# Homepage view
def homepage(request):
    # Fetch the first restaurant entry
    restaurant = Restaurant.objects.first()
    image_url="https://picsum.photos/800/300?"
    return render(request, 'menu.html', {
        'restaurant':restaurant,
        'image_url':image_url
            
    })
#  Menu List View
def menu_list(request):
    # Fetch all the menu items from database
    items = MenuItem.objects.all()
    return render(request, "menu_list.html", {"menu_items": items})

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

# Reservation page view
def reservations(request):
    return render(request, 'reservations.html')
#Custom 404 page view
def custom_404(request, exception):
    return render(request, '404.html', status=404) 

# Feedback Form View
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback') # Reload after submit
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})
