from django.urls import reverse, reverse_lazy
from django.test import TestCase, Client, modify_settings
from task_manager.users.models import CustomUser
from .models import Statuses


@modify_settings(
    MIDDLEWARE={'remove': [
        'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    ]}
)
class StatusesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.status_data = {
            "name": "status test",
        }
        self.user = CustomUser.objects.create(
            username="test1", password="test1")
        self.client.force_login(self.user)
        self.status = Statuses.objects.create(name="test")

    def test_view_label(self):
        response = self.client.get(reverse_lazy('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='statuses/statuses.html')

    def test_create_status(self):
        response = self.client.post(
            reverse_lazy("create_status"),
            self.status_data
        )
        self.assertEqual(response.status_code, 302)
        status = Statuses.objects.get(name=self.status_data["name"])
        self.assertEqual(status.name, self.status_data["name"])
        self.assertRedirects(response, reverse_lazy("statuses"))

    def test_update_status(self):
        url = reverse("update_status", kwargs={"pk": self.status.pk})
        response = self.client.post(url, self.status_data)
        update_status = Statuses.objects.get(pk=self.status.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(update_status.name, self.status_data["name"])
        self.assertRedirects(response, reverse_lazy("statuses"))

    def test_delete_status(self):
        url = reverse("delete_status", args=[self.status.pk])
        response = self.client.post(url, follow=True)
        self.assertRedirects(response, reverse_lazy("statuses"))
        self.assertFalse(Statuses.objects.filter(pk=self.status.pk).exists())
