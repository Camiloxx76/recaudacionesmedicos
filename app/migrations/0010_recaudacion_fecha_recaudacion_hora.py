# Generated by Django 4.2.1 on 2023-06-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_cita_antecedentes_clinicos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recaudacion',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='recaudacion',
            name='hora',
            field=models.TimeField(null=True),
        ),
    ]
