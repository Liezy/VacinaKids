from django.urls import path
from .views import ReportListView, ReportPDFView

urlpatterns = [
    path('', ReportListView.as_view(), name='report_list'),
    path('pdf/', ReportPDFView.as_view(), name='report_pdf'),
]