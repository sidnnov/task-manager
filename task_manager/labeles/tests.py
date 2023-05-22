from django.urls import reverse, reverse_lazy
from django.test import TestCase, Client
from task_manager.users.models import CustomUser
from .models import Labeles


class LabelesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.labele_data = {
            "name": "labele test",
        }
        self.user = CustomUser.objects.create(
            username="test1", password="test1")
        self.client.force_login(self.user)
        self.labeles = Labeles.objects.create(name="test")

    def test_create_labele(self):
        response = self.client.post(
            reverse_lazy("create_labeles"),
            self.labele_data
        )
        self.assertEqual(response.status_code, 302)
        labeles = Labeles.objects.get(name=self.labele_data["name"])
        self.assertEqual(labeles.name, self.labele_data["name"])
        self.assertRedirects(response, reverse_lazy("labeles"))

    def test_labele_update(self):
        url = reverse("update_labele", kwargs={"pk": self.labele.pk})
        response = self.client.post(url, self.labele_data)
        update_labele = Labeles.objects.get(pk=self.labele.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(update_labele.name, self.labele_data["name"])
        self.assertRedirects(response, reverse_lazy("labeles"))
