from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Tasks


# Create your models here.
class Labels(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    label = models.ManyToManyField(Tasks)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("labels")

    def __str__(self):
        return self.name
