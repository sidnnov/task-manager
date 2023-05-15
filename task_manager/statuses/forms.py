from django import forms
from task_manager.statuses.models import Statuses


class StatusModel(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ["title"]
