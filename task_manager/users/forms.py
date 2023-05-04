from django.contrib.auth.forms import UserCreationForm
from task_manager.users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name', 'password1', 'password2')
