from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import ProtectedError

from task_manager.statuses.models import Statuses
from task_manager.utilities import AuthorizationMixin


class StatusesView(AuthorizationMixin, View):
    def get(self, request):
        statuses = Statuses.objects.order_by("id")
        return render(
            request, "statuses/statuses.html", context={"statuses": statuses})


class CreateStatusView(AuthorizationMixin, SuccessMessageMixin, CreateView):
    model = Statuses
    fields = ["name"]
    template_name = "form.html"
    success_message = _("Status successfully created")
    extra_context = {
        "table_name": _("Create status"),
        "button_name": _("Create"),
    }


class UpdateStatusView(AuthorizationMixin, SuccessMessageMixin, UpdateView):
    model = Statuses
    fields = ["name"]
    template_name = "form.html"
    success_message = _("Status successfully changed")
    extra_context = {
        "table_name": _("Changing status"),
        "button_name": _("Change"),
    }


class DeleteStatusView(AuthorizationMixin, SuccessMessageMixin, DeleteView):
    model = Statuses
    template_name = "delete.html"
    success_url = reverse_lazy("statuses")
    success_message = _("Status successfully deleted")
    extra_context = {
        "question": _("Deleting status"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question"] = _("Deleting status")
        context["name"] = self.get_object().name
        return context

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                _("It is impossible to delete a status because it is in use"),
            )
            return redirect("statuses")
