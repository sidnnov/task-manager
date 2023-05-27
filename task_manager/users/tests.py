from django.urls import reverse, reverse_lazy
from django.test import TestCase, Client
from .models import CustomUser


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "Test",
            "password1": "password",
            "password2": "password",
        }
        self.user = CustomUser.objects.create(
            username="test1", password="test1")

    def test_view_label(self):
        response = self.client.get(reverse_lazy('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/users.html')

    def test_user_create(self):
        response = self.client.post(
            reverse_lazy("user_create"),
            self.user_data
        )
        self.assertEqual(response.status_code, 302)
        user = CustomUser.objects.get(username=self.user_data["username"])
        self.assertEqual(user.username, self.user_data["username"])
        self.assertEqual(user.first_name, self.user_data["first_name"])
        self.assertEqual(user.last_name, self.user_data["last_name"])
        self.assertTrue(user.check_password(self.user_data["password1"]))
        self.assertRedirects(response, reverse_lazy("login"))

    def test_user_update(self):
        self.client.force_login(self.user)
        url = reverse("user_update", kwargs={"pk": self.user.pk})
        response = self.client.post(url, self.user_data)
        updated_user = CustomUser.objects.get(pk=self.user.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_user.username, self.user_data["username"])
        self.assertEqual(updated_user.first_name, self.user_data["first_name"])
        self.assertEqual(updated_user.last_name, self.user_data["last_name"])
        self.assertTrue(updated_user.check_password(
            self.user_data["password1"]))
        self.assertRedirects(response, reverse_lazy("users"))

    def test_user_delete(self):
        self.client.force_login(self.user)
        url = reverse("user_delete", args=[self.user.pk])
        response = self.client.post(url, follow=True)
        self.assertRedirects(response, reverse_lazy("users"))
        self.assertFalse(CustomUser.objects.filter(pk=self.user.pk).exists())
