from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from task_manager.users.models import User


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, "users/index.html", context={'users': users})


class UserCreateForm(View):

    def get(self, request):
        return render(request, "users/create.html")


class LoginForm(View):

    def get(self, request):
        return render(request, "users/login.html")
