from django.urls import path
from . import views

urlpatterns = [
    path('', views.VaccineListView.as_view(), name='vaccine_list'),
    path('nova/', views.VaccineCreateView.as_view(), name='vaccine_create'),
    path('<int:pk>/editar/', views.VaccineUpdateView.as_view(), name='vaccine_update'),
    path('<int:pk>/excluir/', views.VaccineDeleteView.as_view(), name='vaccine_delete'),
]