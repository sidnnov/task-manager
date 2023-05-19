from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from task_manager.tasks.forms import TasksForm
from task_manager.tasks.models import Tasks
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class TasksView(View):

    def get(self, request):
        tasks = Tasks.objects.all()
        return render(request, "tasks/tasks.html", context={
            "tasks": tasks})


class CreateTaskView(SuccessMessageMixin, CreateView):
    model = Tasks
    form_class = TasksForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks")
    success_message = _("The task was successfully created")
    extra_context = {
        "table_name": _("Create task"),
        "button_name": _("Create"),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class UpdateTaskView(SuccessMessageMixin, UpdateView):
    model = Tasks
    form_class = TasksForm
    template_name = "tasks/create.html"
    success_message = _("Task successfully changed")
    extra_context = {
        "table_name": _("Changing task"),
        "button_name": _("Change"),
    }


class DeleteTaskView(SuccessMessageMixin, DeleteView):
    model = Tasks
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully deleted")
