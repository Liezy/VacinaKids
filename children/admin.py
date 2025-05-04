from django.contrib import admin
from .models import Child

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'mother_name', 'cpf')
    search_fields = ('name', 'cpf', 'mother_name')
