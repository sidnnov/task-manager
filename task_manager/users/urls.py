from django.urls import path
from task_manager.users.views import IndexView, UserCreateForm, LoginForm


urlpatterns = [
    path("", IndexView.as_view(), name="users"),
    path("create/", UserCreateForm.as_view(), name="user_create"),
    path("login/", LoginForm.as_view(), name="user_login"),
]
