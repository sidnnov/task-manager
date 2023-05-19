from django.urls import path
from task_manager.tasks.views import (
    TasksView,
    CreateTaskView,
)


urlpatterns = [
    path("", TasksView.as_view(), name="tasks"),
    path("create/", CreateTaskView.as_view(), name="create_task"),
    # path("<int:pk>/update/", UpdateStatusView.as_view(), name="update_status"),
    # path("<int:pk>/delete/", DeleteStatusView.as_view(), name="delete_status"),
]
