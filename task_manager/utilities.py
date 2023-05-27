from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


NOT_AUTHORIZED = _("You are not authorized! Please log in.")
DENIED_MESSAGE = _("You have no rights to change another user.")


class AuthorizationMixin(LoginRequiredMixin):
    not_auth_message = NOT_AUTHORIZED
    login_url = "login"

    def get_login_url(self):
        messages.error(self.request, self.not_auth_message)
        return str(self.login_url)


class UserPermissionMixin(UserPassesTestMixin):
    not_auth_message = NOT_AUTHORIZED
    permission_denied_message = DENIED_MESSAGE
    raise_exception = False
    success_url = ""

    def test_func(self):
        obj = self.get_object()
        if hasattr(obj, 'author'):
            return obj.author == self.request.user
        return obj.pk == self.request.user.pk

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_auth_message)
            return redirect("login")
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.success_url)
