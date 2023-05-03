from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from task_manager.users.forms import CustomUserCreationForm
from task_manager.users.models import CustomUser
from django.utils.translation import gettext_lazy as _


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, "users/index.html", context={'users': users})


class UserCreateView(FormView):
    template_name = "users/create.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("user_login")
    extra_context = {
        "table_name": _("Sign up"),
        "button_name": _("Submit"),
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class DeleteUserView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('users')
    template_name = 'users/delete_user.html'


class UpdateUserView(UpdateView):
    model = CustomUser
    template_name = "users/create.html"
    fields = ("username", "first_name", "last_name",)
    extra_context = {
        "table_name": _("Changing user"),
        "button_name": _("Change"),
    }


# class UserCreateForm(FormView):

#     def get(self, request):
#         # form = UserForm()
#         return render(request, "users/create.html")

#     def post(self, request, *args, **kwargs):
#         form = UserForm(request.POST)
#         print(form)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Статья успешно добавлена')
#             return redirect('user_login')
#         return render(request, 'users/create.html', {'form': form})