from django import forms
from .models import Vaccine

class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['name', 'description', 'recommended_age_months']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'recommended_age_months': forms.NumberInput(attrs={'min': 0}),
        }