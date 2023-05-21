from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.db.models import ProtectedError


from task_manager.users.forms import CustomUserCreationForm
from task_manager.users.models import CustomUser


# Create your views here.
class UserPermissionMixin(PermissionRequiredMixin):
    permission_required = "users.change_customuser"
    denied_message = _("You have no rights to change another user.")
    not_auth_message = _("You are not authorized! Please log in.")

    def has_permission(self):
        return self.get_object().pk == self.request.user.pk

    def handle_no_permission(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_auth_message)
            return redirect("login")
        messages.error(self.request, self.denied_message)
        return redirect("users")


class IndexView(View):

    def get(self, request):
        users = CustomUser.objects.all()
        return render(request, "users/users.html", context={"users": users})


class ProfileUserView(View):

    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=kwargs.get("pk"))
        return render(request, "users/profile.html", context={"user": user})


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = "users/create.html"
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


class DeleteUserView(UserPermissionMixin, SuccessMessageMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy("users")
    template_name = "users/delete_user.html"
    success_message = _("User has been successfully deleted")

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request, _("Unable to delete a user because he is being used"))
            return redirect("users")


class UpdateUserView(UserPermissionMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    template_name = "users/create.html"
    form_class = CustomUserCreationForm
    success_message = _("User has been successfully changed")
    extra_context = {
        "table_name": _("Changing user"),
        "button_name": _("Change"),
    }
