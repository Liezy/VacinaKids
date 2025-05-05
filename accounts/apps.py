# accounts/apps.py
import os
from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.contrib.auth import get_user_model
        from django.conf import settings

        User = get_user_model()
        cpf      = getattr(settings, 'ADMIN_CPF', None)
        password = getattr(settings, 'ADMIN_PASSWORD', None)
        email    = getattr(settings, 'ADMIN_EMAIL', None)

        if cpf and password:
            try:
                if not User.objects.filter(cpf=cpf).exists():
                    User.objects.create_superuser(cpf=cpf, password=password, email=email or '')
            except (OperationalError, ProgrammingError):
                pass
