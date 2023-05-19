from django import forms
from task_manager.tasks.models import Tasks
from task_manager.users.models import CustomUser


class TasksForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ["task", "description", "status", "executor"]
