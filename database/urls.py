from django.urls import path

from database import views

app_name = "database"

urlpatterns = [
    path('products', views.list_products, name="list_products"),
]
