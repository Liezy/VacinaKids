import os
from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from django.contrib.auth import get_user_model
        from django.conf import settings

        User = get_user_model()
        cpf      = settings.ADMIN_CPF
        password = settings.ADMIN_PASSWORD

        # só tenta criar se ambas variáveis existirem
        if cpf and password:
            try:
                if not User.objects.filter(cpf=cpf).exists():
                    User.objects.create_superuser(cpf=cpf, password=password, email=email or '')
            except (OperationalError, ProgrammingError):
                # o banco ainda não está pronto (ou rodando migrate não foi chamado)
                # ou outra migração pendente: ignore esse erro
                pass
