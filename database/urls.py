from django.urls import path

from database import views

urlpatterns = [
    path('products', views.list_products, name="list_products"),
]
