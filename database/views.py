from django.db.models import Count
from django.shortcuts import render

from database.models import Category, Product


def list_products(request):
    if request.method == 'POST':
        nav_input = request.POST['nav_input']
        researched_products = Product.objects.filter(name__contains=nav_input)
        return render(request, 'database/products.html',
                      {'nav_input': nav_input, 'researched_products': researched_products})
    else:
        return render(request, 'database/forbidden.html')


def show_product(request, product_id):
    # Retrieve product Id
    product_id = Product.objects.get(pk=product_id)
    return render(request, 'database/show_product.html', {"product": product_id})


def substitute_products(request, product_id):
    # Retrieve product Id
    product_id = Product.objects.get(pk=product_id)
    # Get Product Category
    product_category = Category.objects.filter(product__id=product_id.id)

    substitutes = (
        Product.objects.filter(categories__in=product_category)
            .annotate(nb_cat=Count("categories"))
            .filter(nb_cat__gte=2)
            .filter(score__lt=product_id.score)
            .order_by("score")[:5]
    )

    return render(request, 'database/substitute_products.html', {"product": product_id, "substitutes": substitutes})
