from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import CustomUser


class TestUsersViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            email="user@gmail.com",
            password="Django321",
        )
        self.register_url = reverse("register")
        self.profile_url = reverse("profile")

    def test_registration(self):
        data = {
            "email": "user@gmail.com",
            "password1": "Django321",
            "password2": "Django321",
        }

        self.client.post(self.register_url, data)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.client.force_login(self.user)

    def test_profile_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/profile.html")
