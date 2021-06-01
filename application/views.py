from django.shortcuts import render

from application.models import Article


def list_article(request):
    articles = Article.objects.all()
    return render(request, 'list_article.html', {'articles': articles})


def home_page(request):
    return render(request, 'home.html')
