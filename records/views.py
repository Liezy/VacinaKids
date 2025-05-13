from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import VaccinationRecord
from .forms import VaccinationRecordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

class VaccinationRecordListView(LoginRequiredMixin, ListView):
    model = VaccinationRecord
    template_name = 'records/record_list.html'
    context_object_name = 'records'

class VaccinationRecordCreateView(LoginRequiredMixin, CreateView):
    model = VaccinationRecord
    form_class = VaccinationRecordForm
    template_name = 'records/record_form.html'
    success_url = reverse_lazy('record_list')

class VaccinationRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = VaccinationRecord
    form_class = VaccinationRecordForm
    template_name = 'records/record_form.html'
    success_url = reverse_lazy('record_list')

class VaccinationRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = VaccinationRecord
    template_name = 'records/record_confirm_delete.html'
    success_url = reverse_lazy('record_list')

def health(request):
    return HttpResponse('OK')