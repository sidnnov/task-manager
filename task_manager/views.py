from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View


class HomePageView(TemplateView):

    def get(self, request):
        return render(request, "index.html")


class LoginForm(View):

    def get(self, request):
        return render(request, "users/login.html")
