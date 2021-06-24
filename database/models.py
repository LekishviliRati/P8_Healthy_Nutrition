"""
database/models.py is creating the structure of  database (tables, table fields ...)
"""

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Com."""
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Com."""
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    barcode = models.CharField(max_length=13, unique=True)
    score = models.CharField(max_length=1)
    url = models.URLField()
    image_url = models.URLField()
    small_image_url = models.URLField()
    kcal_100g = models.FloatField(default=0, null=True)
    sugar_100g = models.FloatField(default=0, null=True)
    salt_100g = models.FloatField(default=0, null=True)
    fat_100g = models.FloatField(default=0, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}, {self.score}"


class Favorites(models.Model):
    """Comm."""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product"
    )
    substitute = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="substitute"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user"
    )

    def __str__(self):
        return (
            f"Produit: {self.product}, Substitut: {self.substitute}, User: {self.user}"
        )
