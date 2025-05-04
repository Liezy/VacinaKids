from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginForm
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')