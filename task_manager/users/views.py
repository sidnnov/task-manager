from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from task_manager.users.forms import CustomUserCreationForm
from task_manager.users.models import CustomUser
from django.utils.translation import gettext_lazy as _


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, "users/users.html", context={'users': users})


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = "users/create.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    success_message = _("User is successfully registered")
    extra_context = {
        "table_name": _("Sign up"),
        "button_name": _("Submit"),
    }


class DeleteUserView(SuccessMessageMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('users')
    template_name = 'users/delete_user.html'
    success_message = _("User has been successfully deleted")


class UpdateUserView(SuccessMessageMixin, UpdateView):
    model = CustomUser
    template_name = "users/create.html"
    form_class = CustomUserCreationForm
    success_message = _("User has been successfully changed")
    extra_context = {
        "table_name": _("Changing user"),
        "button_name": _("Change"),
    }
