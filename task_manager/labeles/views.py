from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import ProtectedError
from task_manager.labeles.models import Labeles

from task_manager.labeles.forms import LabelesModel


# Create your views here.
class LabeleLoginMixin(LoginRequiredMixin):
    not_auth_message = _("You are not authorized! Please log in.")

    def handle_no_permission(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_auth_message)
            return redirect("login")


class LabelesView(LabeleLoginMixin, View):
    def get(self, request):
        labeles = Labeles.objects.all()
        return render(request, "labeles/labeles.html", context={"labeles": labeles})


class CreateLabeleView(LabeleLoginMixin, SuccessMessageMixin, FormView):
    template_name = "labeles/create.html"
    form_class = LabelesModel
    success_url = reverse_lazy("labeles")
    success_message = _("Lables successfully created")
    extra_context = {
        "table_name": _("Create labele"),
        "button_name": _("Create"),
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
