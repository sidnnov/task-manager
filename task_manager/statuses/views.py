from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from task_manager.statuses.forms import StatusModel
from task_manager.statuses.models import Statuses
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.
class StatusLoginMixin(LoginRequiredMixin):
    # login_url = reverse_lazy("login")
    not_auth_message = _("You are not authorized! Please log in.")

    def handle_no_permission(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_auth_message)
            return redirect("login")


class StatusesView(StatusLoginMixin, View):

    def get(self, request):
        statuses = Statuses.objects.all()
        return render(request, "statuses/statuses.html", context={
            "statuses": statuses})


class CreateStatusView(StatusLoginMixin, SuccessMessageMixin, FormView):
    template_name = "statuses/create.html"
    form_class = StatusModel
    success_url = reverse_lazy("statuses")
    success_message = _("Status successfully created")
    extra_context = {
        "table_name": _("Create status"),
        "button_name": _("Create"),
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateStatusView(StatusLoginMixin, SuccessMessageMixin, UpdateView):
    model = Statuses
    template_name = "statuses/create.html"
    form_class = StatusModel
    success_message = _("Status successfully changed")
    extra_context = {
        "table_name": _("Changing status"),
        "button_name": _("Change"),
    }


class DeleteStatusView(StatusLoginMixin, SuccessMessageMixin, DeleteView):
    model = Statuses
    template_name = "statuses/delete.html"
    success_url = reverse_lazy("statuses")
    success_message = _("Status successfully deleted")
