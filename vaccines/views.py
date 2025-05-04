from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vaccine
from .forms import VaccineForm
from django.contrib.auth.mixins import LoginRequiredMixin

class VaccineListView(LoginRequiredMixin, ListView):
    model = Vaccine
    template_name = 'vaccines/vaccine_list.html'
    context_object_name = 'vaccines'

class VaccineCreateView(LoginRequiredMixin, CreateView):
    model = Vaccine
    form_class = VaccineForm
    template_name = 'vaccines/vaccine_form.html'
    success_url = reverse_lazy('vaccine_list')

class VaccineUpdateView(LoginRequiredMixin, UpdateView):
    model = Vaccine
    form_class = VaccineForm
    template_name = 'vaccines/vaccine_form.html'
    success_url = reverse_lazy('vaccine_list')

class VaccineDeleteView(LoginRequiredMixin, DeleteView):
    model = Vaccine
    template_name = 'vaccines/vaccine_confirm_delete.html'
    success_url = reverse_lazy('vaccine_list')