# from django import forms
# from task_manager.labels.models import Labels

# from task_manager.statuses.models import Statuses
# from task_manager.tasks.models import Tasks
# from task_manager.users.models import CustomUser


# class TasksForm(forms.ModelForm):
#     status = forms.ModelChoiceField(
#         queryset=Statuses.objects.order_by("id"))
#     executor = forms.ModelChoiceField(
#         queryset=CustomUser.objects.order_by("id"))
#     labels = forms.ModelMultipleChoiceField(
#         queryset=Labels.objects.order_by("id"))

#     class Meta:
#         model = Tasks
#         fields = ["task", "description", "status", "executor", "labels"]
