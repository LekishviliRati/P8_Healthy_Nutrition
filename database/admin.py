from django.contrib import admin
from database.models import Category, Product

# Registered models to access via 'admin' page
admin.site.register(Product)
admin.site.register(Category)
