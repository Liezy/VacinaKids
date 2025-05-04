from django.db import models

class Vaccine(models.Model):
    name = models.CharField("Nome da Vacina", max_length=100)
    description = models.TextField("Descrição", blank=True)
    recommended_age_months = models.PositiveIntegerField("Idade Recomendada (meses)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['recommended_age_months']

    def __str__(self):
        return f"{self.name} ({self.recommended_age_months}m)"