# Generated by Django 4.2.1 on 2023-05-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cita_nombre_recaudacion_concepto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='hora',
            field=models.TimeField(null=True),
        ),
    ]
