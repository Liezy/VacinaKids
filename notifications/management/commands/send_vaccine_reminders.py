# notifications/management/commands/send_vaccine_reminders.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from datetime import timedelta
from django.conf import settings

from django.contrib.auth import get_user_model
from children.models import Child
from vaccines.models import Vaccine
from records.models import VaccinationRecord

User = get_user_model()

class Command(BaseCommand):
    help = 'Envia lembrete único por usuário com próximas vacinas a ≤1 mês'

    def handle(self, *args, **options):
        today = timezone.localdate()
        one_month = timedelta(days=30)

        # Para cada usuário que pediu e‑mail:
        for user in User.objects.filter(receive_email_notifications=True):
            reminders = []

            # para cada criança dele
            for child in user.children.all():
                for vac in Vaccine.objects.all():
                    rec_date = child.birth_date + timedelta(days=vac.recommended_age_months * 30)
                    if today <= rec_date <= today + one_month:
                        if not VaccinationRecord.objects.filter(child=child, vaccine=vac).exists():
                            reminders.append(
                                f"- {child.name}: {vac.name} em {rec_date.strftime('%d/%m/%Y')}"
                            )

            if not reminders:
                continue  # nada a notificar

            subject = "VacinaKids: Próximas vacinas em até 1 mês"
            body = (
                f"Olá {user.first_name or user.username},\n\n"
                "As seguintes vacinas das suas crianças estão com data recomendada "
                "em até 1 mês e ainda não registramos aplicação:\n\n"
                + "\n".join(reminders)
                + "\n\nPor favor, agende-as em tempo.\n\n— VacinaKids"
            )

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            self.stdout.write(f"Enviado lembrete a {user.email}")
