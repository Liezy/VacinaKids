from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginForm
from django.shortcuts import redirect
from django.views.generic import TemplateView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class ConfiguracoesView(TemplateView):
    template_name = 'accounts/configuracoes.html'