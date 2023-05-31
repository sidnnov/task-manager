from django.contrib import admin
from django.urls import path, include
from task_manager.views import HomePageView, UserLoginView, UserLogoutView


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("users/", include("task_manager.users.urls")),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("statuses/", include("task_manager.statuses.urls")),
    path("tasks/", include("task_manager.tasks.urls")),
    path("labels/", include("task_manager.labels.urls")),
]
