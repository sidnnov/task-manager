from django.test import Client, TestCase, modify_settings
from django.urls import reverse, reverse_lazy
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from task_manager.users.models import CustomUser


@modify_settings(
    MIDDLEWARE={'remove': [
        'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    ]}
)
class CreateTaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(
            username="testuser",
            password="testpassword"
        )
        self.client.force_login(self.user)
        self.status = Statuses.objects.create(name="test")
        self.task = Tasks.objects.create(
            task='test1',
            status=self.status,
            executor=self.user,
            author=self.user
        )

    def test_view_label(self):
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/tasks.html')

    def test_create_task(self):
        data = {
            "task": "Test Task",
            "description": "Test Description",
            "status": self.status.id,
            "executor": self.user.id,
        }
        response = self.client.post(reverse_lazy("create_task"), data)

        self.assertEqual(response.status_code, 302)
        task = Tasks.objects.get(task=data["task"])
        self.assertEqual(task.task, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.author, self.user)
        self.assertEqual(task.status.id, self.status.id)
        self.assertEqual(task.executor.id, data["executor"])

    def test_task_update(self):
        status2 = Statuses.objects.create(name="new test")
        user2 = CustomUser.objects.create(
            username="testuser new",
            password="testpassword1"
        )
        url = reverse("update_task", kwargs={"pk": self.task.pk})
        data = {
            "task": "Update Task",
            "description": "Update Description",
            "status": status2.id,
            "executor": user2.id,
        }
        response = self.client.post(url, data)
        update_task = Tasks.objects.get(pk=self.task.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(update_task.task, data["task"])
        self.assertRedirects(response, reverse_lazy("tasks"))

    def test_task_delete(self):
        url = reverse("delete_task", args=[self.task.pk])
        response = self.client.delete(url)
        self.assertRedirects(response, reverse_lazy("tasks"))
        self.assertFalse(Tasks.objects.filter(pk=self.task.pk).exists())
