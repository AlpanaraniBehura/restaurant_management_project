from django.contrib import admin
from .models import Menu, Restaurant, Customer, Feedback, MenuItem

# Register your models here.
admin.site.register(Menu)
admin.site.register(Restaurant)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email') 
admin.site.register(Feedback)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name","price")
    search_fields = ("name",)

