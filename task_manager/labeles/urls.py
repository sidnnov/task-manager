from django.urls import path
from task_manager.labeles.views import (
    LabelesView,
    CreateLabeleView,
    # UpdateLabeleView,
    # DeleteLabeleView,
)


urlpatterns = [
    path("", LabelesView.as_view(), name="labeles"),
    path("create/", CreateLabeleView.as_view(), name="create_labele"),
    # path("<int:pk>/update/", UpdateLabeleView.as_view(), name="update_labele"),
    # path("<int:pk>/delete/", DeleteLabeleView.as_view(), name="delete_labele"),
]
