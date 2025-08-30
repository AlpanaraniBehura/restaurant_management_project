from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from .forms import FeedbackForm, ContactForm
from .models import MenuItem, Restaurant
from django.core.mail import EmailMessage
from django.db.models import Q

# Homepage view
def homepage(request):
    # Fetch the first restaurant entry
    restaurant = Restaurant.objects.first()
    image_url="https://picsum.photos/800/300?"

    query = request.GET.get("q") # get search query
    menu_items = MenuItem.objects.all()
    if query:
        # Simple string comparison(case-insensitive contains)
        words = query.split()
        for word in words:
            menu_items = menu_items.filter(
                Q(name__icontains=word) | Q(description__icontains=word)
            )
    cart = request.session.get("cart",{})
    cart_count = sum(cart_values())

    return render(request, 'menu.html', {
        "restaurant": restaurant,
        "image_url": image_url,
        "menu_items": menu_items,
        "cart_count": cart_count,
        "query": query or ""
    })
#  Menu List View
def menu_list(request):
    # Fetch all the menu items from database
    items = MenuItem.objects.all()
    return render(request, "menu_list.html", {"menu_items": items})

# About page view
def about(request):
    restaurant = Restaurant.objects.first()
    image_url = "https://picsum.photos/800/300?random=2" # Random Placeholder image 
    
    context = {
        'restaurant':restaurant,
        'image_url':image_url,
        'history': "Founded in 2010, our restaurant has been serving delicious meals made from locally sourced ingredients.",
        'mission': "Our mission is to provide a memorable dining experience with fresh, high-quality food and excellent service.",
        'vision': "To be the most loved family restaurant in the city.",
    }
     
    return render(request, 'about.html', context)
    
# Contact us page view
def contact_us(request):r
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

        email_subject = f"New Contact Form Submission from {name}"
        email_body = f"Message: {message}\n\nSender Email: {user_email}"

        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.EMAIL_HOST_USER, # your Gmail account
            to=["ranialpana38@gmail.com"],       # Where you want to receive
            reply_to=[user_email]                # reply goes to user's email
        )
        email.send()

        return redirect("contact_success")
    else:
        form = ContactForm()
    return render(request, "contact_us.html", {"form": form})

def contact_success(request):
    return render(request, "contact_success.html")

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
    return render(request, 'feedback.html', {'form': form})(

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    
    # Increase quantity if item already exist
    cart[item_id] = cart.get(item_id, 0) + 1

    # Save back to session
    request.session['cart'] = cart
    request.session.modified = True

    return redirect("homepage")


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for item_id, qty in cart.items():
        try:
            item = MenuItem.objects.get(id=item_id)
            cart_items.append({"item": item, "quantity": qty})
            total += item.price * qty
        expect MenuItem.DoesNotExist:
            continue
    return render (request, "cart.html", {"cart_items": cart_items, "total": total})





















