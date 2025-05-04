from django.urls import path
from .views import (
    VaccinationRecordListView,
    VaccinationRecordCreateView,
    VaccinationRecordUpdateView,
    VaccinationRecordDeleteView,
)

urlpatterns = [
    path('', VaccinationRecordListView.as_view(), name='record_list'),
    path('nova/', VaccinationRecordCreateView.as_view(), name='record_create'),
    path('<int:pk>/editar/', VaccinationRecordUpdateView.as_view(), name='record_update'),
    path('<int:pk>/excluir/', VaccinationRecordDeleteView.as_view(), name='record_delete'),
]