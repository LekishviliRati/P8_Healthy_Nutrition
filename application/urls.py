from django.urls import path

from application import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('articles', views.list_article, name="list_article"),
]