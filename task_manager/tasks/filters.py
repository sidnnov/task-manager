from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django.forms import CheckboxInput
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from task_manager.users.models import CustomUser


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(
        label=_("Status"),
        queryset=Statuses.objects.all(),
    )
    executor = ModelChoiceFilter(
        label=_("Executor"),
        queryset=CustomUser.objects.all(),
    )
    labels = ModelChoiceFilter(
        label=_("Label"),
        queryset=Labels.objects.all(),
    )
    self_tasks = BooleanFilter(
        label=_("Only your tasks"),
        widget=CheckboxInput,
        method="get_my_tasks",
    )

    def get_my_tasks(self, queryset, _, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Tasks
        fields = ["status", "executor", "labels"]
