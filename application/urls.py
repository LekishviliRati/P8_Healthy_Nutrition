from django.urls import path

from application import views

urlpatterns = [
    path('', views.list_article, name="list_article"),
]