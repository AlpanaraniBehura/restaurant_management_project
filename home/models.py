from django.db import models
from PIL import Image

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
    phone = models.CharField(max_length=15, blank=True, null=True ) # Added field
    address = models.TextField()
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    opening_hours = models.JSONField(default=dict)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True) # Field for logo
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
        return self.comment[:50]  # Show first 50 chars in admin

class MenuItem(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # First save original image

        if self.image:
            img = Image.open(self.image.path)

            # Resize (example: max width=800px)
            max_width = 800
            if img.width > max_width:
                ratio = max_width / float(img.width)
                height = int(float(img.height) * ratio)
                img = img.resize((max_width, height), Image.Resampling.LANCZOS)
                img.save(self.image.path) # Overwrite with resize


class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"
