from django.shortcuts import render
from django.views import View
from .forms import ReportFilterForm
from records.models import VaccinationRecord
from children.models import Child
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin

class ReportListView(LoginRequiredMixin, View):
    template_name = 'reports/report_list.html'

    def get(self, request):
        form = ReportFilterForm(request.GET or None)
        records = VaccinationRecord.objects.select_related('child', 'vaccine')
        age_count = None
        filtered_children = None

        if form.is_valid():
            # filtros de registro
            child = form.cleaned_data.get('child')
            if child:
                records = records.filter(child=child)

            start = form.cleaned_data.get('start_date')
            if start:
                records = records.filter(applied_date__gte=start)

            end = form.cleaned_data.get('end_date')
            if end:
                records = records.filter(applied_date__lte=end)

            # filtros de idade para lista de crianças
            age_min = form.cleaned_data.get('age_min')
            age_max = form.cleaned_data.get('age_max')
            if age_min is not None or age_max is not None:
                today = date.today()
                children_qs = Child.objects.all()
                # idade mínima
                if age_min is not None:
                    cutoff_max = today.replace(year=today.year - age_min)
                    children_qs = children_qs.filter(birth_date__lte=cutoff_max)
                # idade máxima
                if age_max is not None:
                    min_year = today.year - age_max - 1
                    try:
                        cutoff_min = today.replace(year=min_year) + timedelta(days=1)
                    except ValueError:
                        cutoff_min = date(min_year, today.month, today.day) + timedelta(days=1)
                    children_qs = children_qs.filter(birth_date__gte=cutoff_min)
                age_count = children_qs.count()
                filtered_children = children_qs.order_by('name')

        context = {
            'form': form,
            'records': records,
            'age_count': age_count,
            'filtered_children': filtered_children,
        }
        return render(request, self.template_name, context)

class ReportPDFView(LoginRequiredMixin, View):
    def get(self, request):
        # mantém lógica anterior para PDF
        form = ReportFilterForm(request.GET or None)
        records = VaccinationRecord.objects.select_related('child', 'vaccine')
        if form.is_valid():
            child = form.cleaned_data.get('child')
            if child:
                records = records.filter(child=child)
            start = form.cleaned_data.get('start_date')
            if start:
                records = records.filter(applied_date__gte=start)
            end = form.cleaned_data.get('end_date')
            if end:
                records = records.filter(applied_date__lte=end)
        html_string = render_to_string('reports/report_pdf.html', {'records': records, 'form': form})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_vacinacao.pdf"'
        weasyprint.HTML(string=html_string).write_pdf(response)
        return response