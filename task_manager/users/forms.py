from django.contrib.auth.forms import UserCreationForm
from task_manager.users.models import CustomUser
from django import forms
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    # first_name = forms.CharField(
    #     label=_("First name"),
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control is-valid',
    #             'placeholder': _('Enter first name'),
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     label=_("Last name"),
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control', 'placeholder': _('Enter last name')
    #         }
    #     )
    # )
    # username = forms.CharField(
    #     label=_("Username"),
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control', 'placeholder': _('Enter username')
    #         }
    #     )
    # )

    class Meta:
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(
        #         attrs={
        #             'class': 'form-control is-valid',
        #             'placeholder': _('Enter username')
        #         }
        #     ),
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control is-valid',
        #             'placeholder': _('Enter first name')
        #         }
        #     ),
        #     'last_name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control is-valid',
        #             'placeholder': _('Enter last name')
        #         }
        #     ),
        # }
