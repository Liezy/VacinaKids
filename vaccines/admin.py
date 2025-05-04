from django.contrib import admin
from .models import Vaccine

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ('name', 'recommended_age_months', 'created_at')
    list_filter = ('recommended_age_months',)
    search_fields = ('name',)