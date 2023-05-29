from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import CustomUser


class HomePageView(TemplateView):

    def get(self, request):
        return render(request, "index.html")


class UserLoginView(SuccessMessageMixin, LoginView):
    model = CustomUser
    fields = ["username", "password"]
    template_name = "form.html"
    success_url = reverse_lazy("tasks")
    success_message = _("You are logged in")
    extra_context = {
        "table_name": _("Login"),
        "button_name": _("Log in"),
    }


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are unlogged"))
        return super().dispatch(request, *args, **kwargs)
