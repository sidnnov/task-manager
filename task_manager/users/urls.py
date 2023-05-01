from django.urls import path
from task_manager.users.views import (
    IndexView,
    UserCreateView,
    UpdateUserView,
    LoginForm,
    DeleteUserView
)


urlpatterns = [
    path("", IndexView.as_view(), name="users"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("<int:pk>/update/", UpdateUserView.as_view(), name="user_update"),
    path("<int:pk>/delete/", DeleteUserView.as_view(), name="user_delete"),
    path("login/", LoginForm.as_view(), name="user_login"),
]
