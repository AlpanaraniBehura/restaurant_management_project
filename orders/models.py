from django.db import models
from django.contrib.auth.models import User
from products.models import Item

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
         ('pending', 'pending'),
         ('preparing', 'preparing'),
         ('delivered', 'delivered'),
         ('cancelled', 'cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
   
    def __str__(self):
        return f"{self.quantity} x {self.item.item_name} (Order #{self.order.id})"