from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import ProtectedError
from task_manager.labels.models import Labels


# Create your views here.
class LabelLoginMixin(LoginRequiredMixin):
    not_auth_message = _("You are not authorized! Please log in.")

    def handle_no_permission(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_auth_message)
            return redirect("login")


class LabelsView(LabelLoginMixin, View):
    def get(self, request):
        labels = Labels.objects.all()
        return render(
            request, "labels/labels.html", context={"labels": labels})


class CreateLabelView(LabelLoginMixin, SuccessMessageMixin, CreateView):
    model = Labels
    template_name = "labels/create.html"
    fields = ["name"]
    success_url = reverse_lazy("labels")
    success_message = _("Label successfully created")
    extra_context = {
        "table_name": _("Create label"),
        "button_name": _("Create"),
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateLabelView(LabelLoginMixin, SuccessMessageMixin, UpdateView):
    model = Labels
    fields = ["name"]
    template_name = "labels/create.html"
    success_message = _("Label successfully changed")
    extra_context = {
        "table_name": _("Changing label"),
        "button_name": _("Change"),
    }


class DeleteLabelView(LabelLoginMixin, SuccessMessageMixin, DeleteView):
    model = Labels
    template_name = "labels/delete.html"
    success_url = reverse_lazy("labels")
    success_message = _("Label successfully deleted")

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                _("It is impossible to delete a label because it is in use"),
            )
            return redirect("labels")
