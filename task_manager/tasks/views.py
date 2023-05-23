from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from task_manager.tasks.forms import TasksCreateForm, TasksFilterForm
from task_manager.tasks.models import Tasks


# Create your views here.
class TaskLoginMixin(LoginRequiredMixin):
    not_auth_message = _("You are not authorized! Please log in.")

    def handle_no_permission(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_auth_message)
            return redirect("login")


class TasksView(TaskLoginMixin, View):
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


class TaskCardView(TaskLoginMixin, View):
    def get(self, request, *args, **kwargs):
        task = Tasks.objects.get(pk=kwargs.get("pk"))
        return render(request, "tasks/card.html", context={"task": task})


class CreateTaskView(TaskLoginMixin, SuccessMessageMixin, CreateView):
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


class UpdateTaskView(TaskLoginMixin, SuccessMessageMixin, UpdateView):
    model = Tasks
    form_class = TasksCreateForm
    template_name = "tasks/create.html"
    success_message = _("Task successfully changed")
    extra_context = {
        "table_name": _("Changing task"),
        "button_name": _("Change"),
    }


class DeleteTaskView(
    TaskLoginMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = Tasks
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully deleted")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_auth_message)
            return redirect("login")
        messages.error(self.request,
                       _("The task can be deleted only by its author"))
        return redirect(self.success_url)
