from django import forms
from .models import VaccinationRecord
from children.models import Child
from vaccines.models import Vaccine

class VaccinationRecordForm(forms.ModelForm):
    class Meta:
        model = VaccinationRecord
        fields = ['child', 'vaccine', 'applied_date']
        widgets = {
            'applied_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['child'].queryset = Child.objects.order_by('name')
        self.fields['vaccine'].queryset = Vaccine.objects.order_by('name')