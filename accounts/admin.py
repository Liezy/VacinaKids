from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        ('Pessoais', {'fields': ('first_name', 'last_name', 'email', 'receive_email_notifications')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'password1', 'password2'),
        }),
    )
    list_display = ('cpf', 'first_name', 'last_name', 'is_staff')
    search_fields = ('cpf', 'first_name', 'last_name')
    ordering = ('cpf',)
    readonly_fields = ('date_joined',)