from django import forms
from task_manager.labels.models import Labels


class LabelsModel(forms.ModelForm):
    class Meta:
        model = Labels
        fields = ["name"]
