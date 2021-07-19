from django.db import IntegrityError
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from application.models import Category, Product, Favorites
from accounts.models import CustomUser as User


def home_page(request):
    return render(request, 'application/home.html')


def legal_notices(request):
    return render(request, 'application/legal_notices.html')


def contact(request):
    return render(request, 'application/contact.html')


def list_products(request):
    if request.method == 'POST':
        nav_input = request.POST['nav_input']
        researched_products = Product.objects.filter(name__contains=nav_input)
        return render(request, 'application/list_products.html',
                      {'nav_input': nav_input, 'researched_products': researched_products})
    else:
        return render(request, 'application/forbidden.html')


def show_product(request, product_id):
    product_id = Product.objects.get(pk=product_id)
    return render(request, 'application/product_page.html', {"product": product_id})


def substitute_products(request, product_id):
    product_id = Product.objects.get(pk=product_id)
    product_category = Category.objects.filter(product__id=product_id.id)

    substitutes = (
        Product.objects.filter(categories__in=product_category)
        .annotate(nb_cat=Count("categories"))
        .filter(nb_cat__gte=2)
        .filter(score__lt=product_id.score)
        .order_by("score")[:5]
    )

    return render(request, 'application/substitute_products.html', {"product": product_id, "substitutes": substitutes})


@login_required
def add_to_favorites_page(request, product_id, substitute_id):
    """Comment."""
    product = Product.objects.get(pk=product_id)
    substitute = Product.objects.get(pk=substitute_id)
    user = User.objects.get(
        pk=request.user.id
    )
    favorite = Favorites(product=product, substitute=substitute, user=user)

    try:
        favorite.save()
        return redirect('favorites')
    except IntegrityError:
        return render(request, 'application/forbidden.html')


@login_required
def delete_from_favorites_page(request, product_id, substitute_id):
    """Comment."""
    product = Product.objects.get(pk=product_id)
    substitute = Product.objects.get(pk=substitute_id)
    user = User.objects.get(
        pk=request.user.id
    )
    # favorite = Favorites(product=product, substitute=substitute, user=user)
    favorite = Favorites.objects.filter(product=product, substitute=substitute, user=user)

    try:
        favorite.delete()
        return redirect('favorites')
    except IntegrityError:
        return render(request, 'application/forbidden.html')


@login_required
def favorites_page(request):
    """Comment."""
    user_id = User.objects.get(pk=request.user.id)
    favorites = Favorites.objects.filter(user_id=user_id)

    return render(request, 'application/favorites.html', {'favorites': favorites})
