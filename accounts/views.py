from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginForm, NotificationSettingsForm
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class ConfiguracoesView(TemplateView):
    template_name = 'accounts/configuracoes.html'

class NotificationSettingsView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = NotificationSettingsForm
    template_name = 'accounts/notification_settings.html'
    success_url = reverse_lazy('notification_settings')

    def get_object(self):
        return self.request.user