from django.db import models

class Child(models.Model):
    name = models.CharField("Nome", max_length=100)
    birth_date = models.DateField("Data de Nascimento")
    mother_name = models.CharField("Nome da Mãe", max_length=150)
    cpf = models.CharField("CPF", max_length=11, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.birth_date.strftime('%d/%m/%Y')})"
