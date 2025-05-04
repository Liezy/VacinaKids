from django import forms
from .models import Child

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'birth_date', 'mother_name', 'cpf']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
