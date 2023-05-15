from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class HomePageView(TemplateView):

    def get(self, request):
        return render(request, "index.html")


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    success_message = _("You are logged in")


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are unlogged"))
        return super().dispatch(request, *args, **kwargs)
