"""project_files URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from database import views as database_views
from application import views as application_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('application.urls')),
    path('home/', application_views.home_page, name="home_page"),
    # redirect with include function to urls.py of application home page called.
    path('products/', database_views.list_products, name='list_products'),
    path('product_page/<int:product_id>/', database_views.show_product, name='show_product'),
    path('subtitute_product_page/<int:product_id>/', database_views.substitute_products, name='substitute_products'),
    path('favorites/', database_views.favorites_page, name='favorites'),
    path('addfavorite/<int:product_id>/<int:substitute_id>/', database_views.add_to_favorites_page, name='addfavorite'),
]
