# Generated by Django 4.2.1 on 2023-06-03 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_recaudacion_fecha_recaudacion_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='user',
        ),
    ]
