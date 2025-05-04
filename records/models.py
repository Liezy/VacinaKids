from django.db import models
from django.utils import timezone
from children.models import Child
from vaccines.models import Vaccine

class VaccinationRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='records')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.PROTECT, related_name='records')
    applied_date = models.DateField("Data de Aplicação", default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-applied_date']
        verbose_name = 'Registro de Vacinação'
        verbose_name_plural = 'Registros de Vacinação'

    def __str__(self):
        return f"{self.child.name} - {self.vaccine.name} em {self.applied_date.strftime('%d/%m/%Y')}"