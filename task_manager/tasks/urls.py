from django.urls import path
from task_manager.tasks.views import (
    TasksView,
    CreateTaskView,
    UpdateTaskView,
    DeleteTaskView,
    TaskCardView,
)


urlpatterns = [
    path("", TasksView.as_view(), name="tasks"),
    path("create/", CreateTaskView.as_view(), name="create_task"),
    path("<int:pk>/update/", UpdateTaskView.as_view(), name="update_task"),
    path("<int:pk>/delete/", DeleteTaskView.as_view(), name="delete_task"),
    path("<int:pk>/", TaskCardView.as_view(), name="card_task"),
]
