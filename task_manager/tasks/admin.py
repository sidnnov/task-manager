from django.contrib import admin
from task_manager.tasks.models import LabelForTask, Tasks


# Register your models here.
admin.site.register(Tasks)
admin.site.register(LabelForTask)
