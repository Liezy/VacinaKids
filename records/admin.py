from django.contrib import admin
from .models import VaccinationRecord

@admin.register(VaccinationRecord)
class VaccinationRecordAdmin(admin.ModelAdmin):
    list_display = ('child', 'vaccine', 'applied_date')
    list_filter = ('vaccine', 'applied_date')
    search_fields = ('child__name', 'vaccine__name')