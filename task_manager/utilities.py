from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class AuthorizationMixin(LoginRequiredMixin):
    not_auth_message = _("You are not authorized! Please log in.")

    def handle_no_permission(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_auth_message)
            return redirect("login")
