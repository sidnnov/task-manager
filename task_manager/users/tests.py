from django.test import TestCase
from django.urls import reverse_lazy
from .models import CustomUser
from django.test import Client


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = Client()

    def test_create_users(self):
        response = self.client.post(reverse_lazy('user_create'), {
            'username': "test_1",
            'first_name': "first",
            'last_name': "last",
            'password1': "123",
            'password2': "123",
            }, follow=True
        )
        user = CustomUser.objects.get(username='test_1')
        self.assertEqual(user.username, 'test_1')
        self.assertEqual(user.first_name, 'first')
        self.assertEqual(user.last_name, 'last')
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_users(self):
        response = self.client.post(reverse_lazy('user_update'), {
            'username': "test_1",
            'first_name': "first",
            'last_name': "last",
            'password1': "123",
            'password2': "123",
            }, follow=True
        )
        self.assertRedirects(response, reverse_lazy('login'))
    # def test_delete_users(self):
    #     user = CustomUser.objects.get(first_name="John")
    #     user.delete()
    #     self.assertEqual(user.id, None)
