from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.tasks.forms import TasksCreateForm, TasksFilterForm
from task_manager.tasks.models import Tasks
from task_manager.utilities import AuthorizationMixin, UserPermissionMixin


# Create your views here.
class TasksView(AuthorizationMixin, View):
    def get(self, request):
        tasks = Tasks.objects.all()
        form = TasksFilterForm(request.GET)

        status = request.GET.get("status")
        executor = request.GET.get("executor")
        labels = request.GET.get("labels")
        self_tasks = request.GET.get("self_tasks")

        if status:
            tasks = tasks.filter(status=status)
        if executor:
            tasks = tasks.filter(executor=executor)
        if labels:
            tasks = tasks.filter(labels=labels)
        if self_tasks and self_tasks == "on":
            tasks = tasks.filter(author=request.user)

        context = {
            "tasks": tasks,
            "form": form,
            "selected_status": status,
            "selected_executor": executor,
            "selected_label": labels,
            "self_tasks": self_tasks,
        }
        return render(request, "tasks/tasks.html", context)


class TaskCardView(AuthorizationMixin, View):

    def get(self, request, *args, **kwargs):
        task = Tasks.objects.get(pk=kwargs.get("pk"))
        return render(request, "tasks/card.html", context={"task": task})


class CreateTaskView(AuthorizationMixin, SuccessMessageMixin, CreateView):
    model = Tasks
    form_class = TasksCreateForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks")
    success_message = _("The task was successfully created")
    extra_context = {
        "table_name": _("Create task"),
        "button_name": _("Create"),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(AuthorizationMixin, SuccessMessageMixin, UpdateView):
    model = Tasks
    form_class = TasksCreateForm
    template_name = "tasks/create.html"
    success_message = _("Task successfully changed")
    extra_context = {
        "table_name": _("Changing task"),
        "button_name": _("Change"),
    }


class DeleteTaskView(UserPermissionMixin, SuccessMessageMixin, DeleteView):
    model = Tasks
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully deleted")
    permission_denied_message = _("The task can be deleted only by its author")
