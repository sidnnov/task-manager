from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.db.models import ProtectedError


from task_manager.users.forms import CustomUserCreationForm
from task_manager.users.models import CustomUser
from task_manager.utilities import UserPermissionMixin


# Create your views here.
class IndexView(View):

    def get(self, request):
        users = CustomUser.objects.all()
        return render(request, "users/users.html", context={"users": users})


class ProfileUserView(View):

    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=kwargs.get("pk"))
        return render(request, "users/profile.html", context={"user": user})


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = "form.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    success_message = _("User is successfully registered")
    extra_context = {
        "table_name": _("Sign up"),
        "button_name": _("Submit"),
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateUserView(UserPermissionMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    success_url = reverse_lazy("users")
    template_name = "form.html"
    form_class = CustomUserCreationForm
    success_message = _("User has been successfully changed")
    extra_context = {
        "table_name": _("Changing user"),
        "button_name": _("Change"),
    }


class DeleteUserView(UserPermissionMixin, SuccessMessageMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy("users")
    template_name = "delete.html"
    success_message = _("User has been successfully deleted")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question"] = _("Deleting a user")
        context["name"] = self.get_object().get_full_name
        return context

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request, _("Unable to delete a user because he is being used"))
            return redirect("users")
