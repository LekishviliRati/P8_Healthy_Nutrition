from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)