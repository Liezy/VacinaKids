from django.urls import path
from .views import CustomLoginView, CustomLogoutView, ConfiguracoesView, NotificationSettingsView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('configuracoes/', ConfiguracoesView.as_view(), name='configuracoes'),
    path('settings/notifications/', NotificationSettingsView.as_view(), name='notification_settings'),
]