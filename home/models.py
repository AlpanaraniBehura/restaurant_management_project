from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Customer's name for dine-in or guest orders."
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        help_text="Customer's phone number for contact or tracking."
    )
    email = models.EmailField(
        blank = True,
        null = True,
        help_text = "Customer's email for receipts or marketing."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Time when the customer record was created."
    )
    def __str__(self):
        # If name exists,show it,else fallback to phone or 'Guest'
        return self.name or self.phone or "Guest Customer"
    class Meta:
        ordering = ['-created_at']
        verbose_name="Customer"
        verbose_name_plural = "Customers"
class Feedback(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment[:50]  #Show first 50 chars in admin

class MenuItem(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"
