from django import forms
from children.models import Child

class ReportFilterForm(forms.Form):
    child = forms.ModelChoiceField(
        queryset=Child.objects.order_by('name'),
        required=False,
        label='Filtrar por Criança'
    )
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Data Inicial'
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Data Final'
    )
    age_min = forms.IntegerField(
        required=False,
        min_value=0,
        label='Idade Mínima (anos)'
    )
    age_max = forms.IntegerField(
        required=False,
        min_value=0,
        label='Idade Máxima (anos)'
    )