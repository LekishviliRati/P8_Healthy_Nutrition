from django.test import TestCase

from accounts.models import CustomUser


class ModelsTestCase(TestCase):
    def test_user_email(self):
        user = CustomUser.objects.create(
            email="user@gmail.com",
            password="Django321",
        )
        self.assertEqual(user.email, "user@gmail.com")

    def test_superuser_is_staff(self):
        superuser = CustomUser.objects.create_superuser(
            email="superuser@gmail.com",
            password="Django321",
        )
        self.assertIs(superuser.is_staff, True)

    def test_user_not_staff(self):
        user = CustomUser.objects.create_user(
            email="user@gmail.com",
            password="Django321",
        )
        self.assertIs(user.is_staff, False)
