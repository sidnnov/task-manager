from django.urls import path
from task_manager.users.views import (
    IndexView,
    UserCreateView,
    UpdateUserView,
    DeleteUserView,
    ProfileUserView,
)


urlpatterns = [
    path("", IndexView.as_view(), name="users"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("<int:pk>/update/", UpdateUserView.as_view(), name="user_update"),
    path("<int:pk>/delete/", DeleteUserView.as_view(), name="user_delete"),
    path("<int:pk>/", ProfileUserView.as_view(), name="user_profile"),
]
