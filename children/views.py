from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Child
from .forms import ChildForm
from collections import defaultdict
from django.utils import timezone
from datetime import timedelta
from vaccines.models import Vaccine
from records.models import VaccinationRecord
from django.contrib.auth.mixins import LoginRequiredMixin

class ChildListView(LoginRequiredMixin, ListView):
    model = Child
    template_name = 'children/child_list.html'
    context_object_name = 'children'

class ChildCreateView(LoginRequiredMixin, CreateView):
    model = Child
    form_class = ChildForm
    template_name = 'children/child_form.html'
    success_url = reverse_lazy('child_list')

class ChildUpdateView(LoginRequiredMixin, UpdateView):
    model = Child
    form_class = ChildForm
    template_name = 'children/child_form.html'
    success_url = reverse_lazy('child_list')

class ChildDeleteView(LoginRequiredMixin, DeleteView):
    model = Child
    template_name = 'children/child_confirm_delete.html'
    success_url = reverse_lazy('child_list')

class ChildDetailView(LoginRequiredMixin, DetailView):
    model = Child
    template_name = 'children/child_detail.html'
    context_object_name = 'child'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        child = self.object
        today = timezone.localdate()

        # Agrupa vacinas por idade recomendada (meses)
        schedule_by_age = defaultdict(list)

        for vac in Vaccine.objects.all():
            rec_date = child.birth_date + timedelta(days=vac.recommended_age_months * 30)
            try:
                record = VaccinationRecord.objects.get(child=child, vaccine=vac)
                applied = record.applied_date
            except VaccinationRecord.DoesNotExist:
                applied = None

            if applied:
                status = 'Aplicada'
            else:
                status = 'Atrasada' if today > rec_date else 'Futura'

            schedule_by_age[vac.recommended_age_months].append({
                'vaccine': vac,
                'recommended_date': rec_date,
                'applied_date': applied,
                'status': status,
            })

        # Ordena por idade
        ordered_schedule = sorted(schedule_by_age.items(), key=lambda x: x[0])
        context['schedule_by_age'] = ordered_schedule
        return context