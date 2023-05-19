from django.db import models
from django.urls import reverse
from task_manager.statuses.models import Statuses
from task_manager.users.models import CustomUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Tasks(models.Model):
    task_name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True)
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT, verbose_name=_("Status"))
    performer = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, related_name="performed_tasks", verbose_name=_("Performer"))
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("tasks")
