# Generated by Django 5.2 on 2025-05-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='receive_email_notifications',
            field=models.BooleanField(default=False, verbose_name='Receber email de notificações'),
        ),
    ]
