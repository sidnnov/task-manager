from django.contrib.auth.views import LoginView
# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib import messages
# from django.views import View


class HomePageView(TemplateView):

    def get(self, request):
        return render(request, "index.html")


class LoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
