from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from .forms import UserAdminCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin  # - baseado em classe
# from django.contrib.auth.decorators import login_required - Baseado em função


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self, queryset=None):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm
    # queryset = User.objects.none()  # Adicione esta linha

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        return self.request.user  # Retorna o usuário logado


index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()



