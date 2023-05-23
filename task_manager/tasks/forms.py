from django import forms
from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import CustomUser


class TasksCreateForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ["task", "description", "status", "executor", "labels"]


class TasksFilterForm(forms.Form):
    status = forms.ModelChoiceField(
        queryset=Statuses.objects.all(),
        required=False,
    )
    executor = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        required=False,
    )
    labels = forms.ModelChoiceField(
        queryset=Labels.objects.all(),
        required=False,
    )
    self_tasks = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"].empty_label = _("All")
        self.fields["status"].label = _("Status")
        self.fields["executor"].empty_label = _("All")
        self.fields["executor"].label = _("Executor")
        self.fields["labels"].empty_label = _("All")
        self.fields["labels"].label = _("Label")
        self.fields["self_tasks"].label = _("Only your tasks")
