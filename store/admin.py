from django.contrib import admin  # Imports Django’s admin functionality
from .models import Product, Category, Customer, Order  # Imports the Product class model from the models.py

admin.site.register(Product)  # Registers the Product model to show up in the admin dashboard
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
# Register your models here.
