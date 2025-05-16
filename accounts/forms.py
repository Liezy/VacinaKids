from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='CPF', max_length=11,
        widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Senha', strip=False,
        widget=forms.PasswordInput)
    
class NotificationSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['receive_email_notifications']