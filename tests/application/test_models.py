from django.test import TestCase

from application.models import Product, Category, Favorites
from accounts.models import CustomUser


class ModelsTestCase(TestCase):
    def test_category_table(self):
        category = Category.objects.create(
            name="Beverages",
        )
        self.assertEqual(category.name, "Beverages")

    def test_product_table(self):
        product = Product.objects.create(
            name="Muesli raisin",
            brand="Bjorg",
            barcode="3229820129488",
            score="A",
            url="https://fr.openfoodfacts.org/produit/3229820129488/muesli-raisin-figue-abricot-bjorg",
            image_url="https://images.openfoodfacts.org/images/products/322/982/012/9488/front_fr.166.400.jpg",
            small_image_url="https://images.openfoodfacts.org/images/products/322/982/012/9488/front_fr.166.200.jpg",
            kcal_100g=0.0,
            sugar_100g=0.0,
            salt_100g=0.03,
            fat_100g=6.3,
        )
        self.assertEqual(product.name, "Muesli raisin")
        self.assertEqual(product.brand, "Bjorg")
        self.assertEqual(product.barcode, "3229820129488")
        self.assertEqual(product.score, "A")

    def test_favorite_table(self):
        product = Product.objects.create(
            name="Chocapic", barcode="7613034626844", score="B"
        )
        substitute = Product.objects.create(
            name="Flocons", barcode="3229820019307", score="A"
        )
        user = CustomUser.objects.create(
            email="user@gmail.com", password="Django321"
        )
        favorite = Favorites.objects.create(
            product=product, substitute=substitute, user=user
        )
        self.assertEqual(str(favorite),
                         f"Produit: {favorite.product}, Substitut: {favorite.substitute}, User: {favorite.user}",
                         )
