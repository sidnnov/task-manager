from django.urls import reverse, reverse_lazy
from django.test import TestCase, Client

from task_manager.users.models import CustomUser
from .models import Statuses


class StatusesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.status_data = {
            "title": "status test",
        }
        self.user = CustomUser.objects.create(
            username="test1", password="test1")
        self.client.force_login(self.user)
        self.status = Statuses.objects.create(title="test")

    def test_create_status(self):
        response = self.client.post(
            reverse_lazy("create_status"),
            self.status_data
        )
        self.assertEqual(response.status_code, 302)
        status = Statuses.objects.get(title=self.status_data["title"])
        self.assertEqual(status.title, self.status_data["title"])
        self.assertRedirects(response, reverse_lazy("statuses"))

    def test_user_update(self):
        url = reverse("update_status", kwargs={"pk": self.status.pk})
        response = self.client.post(url, self.status_data)
        update_status = Statuses.objects.get(pk=self.status.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(update_status.title, self.status_data["title"])
        self.assertRedirects(response, reverse_lazy("statuses"))

    def test_user_delete(self):
        url = reverse("delete_status", args=[self.status.pk])
        response = self.client.post(url, follow=True)
        self.assertRedirects(response, reverse_lazy("statuses"))
        self.assertFalse(Statuses.objects.filter(pk=self.status.pk).exists())
