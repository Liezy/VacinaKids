from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChildListView.as_view(), name='child_list'),
    path('novo/', views.ChildCreateView.as_view(), name='child_create'),
    path('<int:pk>/', views.ChildDetailView.as_view(), name='child_detail'),
    path('<int:pk>/editar/', views.ChildUpdateView.as_view(), name='child_update'),
    path('<int:pk>/excluir/', views.ChildDeleteView.as_view(), name='child_delete'),
]