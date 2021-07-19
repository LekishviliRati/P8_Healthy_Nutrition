from django.test import TestCase, Client
from django.urls import reverse

from application.models import Product
from accounts.models import CustomUser


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            email="user@gmail.com",
            password="Django321",
        )
        Product.objects.create(id=95, name="Cracotte", score="C")
        self.home_page_url = reverse("home_page")
        self.products_list_url = reverse("list_products")
        self.substitute_products_url = \
            reverse("substitute_products", args=[95])
        self.product_page_url = reverse("product_page", args=[95])
        self.favorites_list_url = reverse("favorites")
        self.legal_notices_url = reverse("legal_notices")
        self.contact_url = reverse("contact")

    def test_home_page(self):
        response = self.client.get(self.home_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "application/home.html")

    def test_products_list_page_POST(self):
        searched_product = {"nav_input": "data"}

        response = self.client.post(
            self.products_list_url, data=searched_product
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "application/list_products.html")

    def test_substitutes_products_page(self):
        response = self.client.get(self.substitute_products_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "application/substitute_products.html")

    def test_product_page(self):
        response = self.client.get(self.product_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"].name, "Cracotte")
        self.assertTemplateUsed(response, "application/product_page.html")

    def test_save_substitute_success(self):
        self.client.force_login(self.user)
        product = Product.objects.create(
            name="Noir extra", score="E", barcode="3664346305860"
        )
        substitute = Product.objects.create(
            name="Biscuit pomme noisette", score="A", barcode="3175681851849"
        )
        url = reverse(
            "addfavorite",
            args=(
                product.id,
                substitute.id,
            ),
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_favorites_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.favorites_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "application/favorites.html")

    def test_legal_notice_page(self):
        response = self.client.get(self.legal_notices_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "application/legal_notices.html")

    def test_contact_page(self):
        response = self.client.get(self.contact_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "application/contact.html")
