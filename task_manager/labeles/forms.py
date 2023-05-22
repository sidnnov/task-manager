from django import forms
from task_manager.labeles.models import Labeles


class LabelesModel(forms.ModelForm):
    class Meta:
        model = Labeles
        fields = ["name"]
