from django.urls import path
from application import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
]
