# Generated by Django 5.0.3 on 2024-04-03 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_est_vip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='devise',
        ),
    ]