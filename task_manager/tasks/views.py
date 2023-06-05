from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

from django_filters.views import FilterView
from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.models import Tasks
from task_manager.users.models import CustomUser
from task_manager.utilities import AuthorizationMixin, UserPermissionMixin


class TasksView(AuthorizationMixin, FilterView):
    model = Tasks
    context_object_name = "tasks"
    template_name = "tasks/tasks.html"
    filterset_class = TaskFilter
    ordering = ["id"]


class TaskCardView(AuthorizationMixin, View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Tasks, pk=kwargs.get("pk"))
        return render(request, "tasks/card.html", context={"task": task})


class TaskFormMixin:
    model = Tasks
    fields = ["name", "description", "status", "executor", "labels"]
    template_name = "form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["status"].queryset = Statuses.objects.order_by("id")
        form.fields["executor"].queryset = CustomUser.objects.order_by("id")
        form.fields["executor"].required = False
        form.fields["labels"].queryset = Labels.objects.order_by("id")
        return form


class CreateTaskView(
    AuthorizationMixin, SuccessMessageMixin, TaskFormMixin, CreateView
):
    success_message = _("The task was successfully created")
    extra_context = {
        "table_name": _("Create task"),
        "button_name": _("Create"),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(
    AuthorizationMixin, SuccessMessageMixin, TaskFormMixin, UpdateView
):
    success_message = _("Task successfully changed")
    extra_context = {
        "table_name": _("Changing task"),
        "button_name": _("Change"),
    }


class DeleteTaskView(UserPermissionMixin, SuccessMessageMixin, DeleteView):
    model = Tasks
    template_name = "delete.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully deleted")
    permission_denied_message = _("The task can be deleted only by its author")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question"] = _("Deleting task")
        context["name"] = self.get_object().name
        return context
