from django.core.management.base import BaseCommand
from django.db import IntegrityError
from application.models import Category, Product
from application.api import Api


class Command(BaseCommand):
    def handle(self, *args, **options):
        """"""
        self.clear_db()
        self.save_products()

    def clear_db(self):
        """Reset Database."""

        all_products = Product.objects.all()
        all_products.delete()

        all_categories = Category.objects.all()
        all_categories.delete()

        print(" 🧹🧽 Nettoyage de la base de données : OK")

    def save_products(self):
        """Save products and categories in Database."""

        api_class = Api()
        products_and_categories_from_api = api_class.download_products()

        if products_and_categories_from_api is not None:
            print(" ✅  Les produits ont été téléchargé avec succès depuis l'API")
        else:
            print(" ❌ -> Les produits n'ont pas pu être téléchargés depuis l'API")

        for product in products_and_categories_from_api:
            name = product.get("product_name_fr")[:150].strip().lower().capitalize()
            brands = product.get("brands")[:150].strip().lower().capitalize()
            grade = product.get("nutriscore_grade")[0].upper()
            barcode = product.get("code")[:13].strip()
            url = product.get("url")
            picture = product.get("image_url")
            small_picture = product.get("image_small_url")
            categories = categories = [
                name.strip().lower().capitalize()
                for name in product["categories"].split(",")
            ]

            selected_nutriments = [
                "energy_100g",
                "sugars_100g",
                "fat_100g",
                "salt_100g",
            ]

            nutriments_dict = {}

            for nutriment in selected_nutriments:
                nutriment_value = product.get("nutriments").get(nutriment)
                if isinstance(nutriment_value, float) is True:
                    value = nutriment_value
                else:
                    value = 0
                nutriments_dict[nutriment] = value

            product_instance = Product(
                name=name,
                brand=brands,
                barcode=barcode,
                score=grade,
                url=url,
                image_url=picture,
                small_image_url=small_picture,
                kcal_100g=nutriments_dict.get("energy_100g"),
                sugar_100g=nutriments_dict.get("sugars_100g"),
                salt_100g=nutriments_dict.get("salt_100g"),
                fat_100g=nutriments_dict.get("fat_100g"),
            )

            try:
                product_instance.save()

                saved_categories = []
                for category in categories:
                    category_instance = Category(name=category)
                    if category not in saved_categories:
                        saved_categories.append(category)
                        try:
                            category_instance.save()
                        except IntegrityError:
                            category_instance = Category.objects.get(name=category)

                        # Link products to categories
                        product_instance.categories.add(category_instance)
                        product_instance.save()
            except IntegrityError:
                continue

        print("😎 -> LA BASE DE DONNÉES EST COMPLÉTÉE ! <- 😎")
