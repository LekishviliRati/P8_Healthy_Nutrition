"""better_nutrition URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views as auth_views
import accounts.views as accounts_views
import application.views as application_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),
    path('legal_notices/', application_views.legal_notices, name='legal_notices'),
    path('contact/', application_views.contact, name='contact'),
    path('register/', accounts_views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='application/home.html'), name='logout'),
    path('accounts/profile/', accounts_views.profile, name="profile"),
    path('list_products/', application_views.list_products, name="list_products"),
    path('product_page/<int:product_id>/', application_views.show_product, name='product_page'),
    path('subtitute_products/<int:product_id>/', application_views.substitute_products, name='substitute_products'),
    path('add_favorite/<int:product_id>/<int:substitute_id>/',
         application_views.add_to_favorites_page, name='addfavorite'),
    path('delete_favorite/<int:product_id>/<int:substitute_id>/',
         application_views.delete_from_favorites_page, name='deletefavorite'),
    path('favorites/', application_views.favorites_page, name='favorites'),

]
