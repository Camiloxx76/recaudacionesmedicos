# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Cita, Medico, Recaudacion

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora', 'medico')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad']

@admin.register(Recaudacion)
class RecaudacionAdmin(admin.ModelAdmin):
    list_display = ('medico', 'fecha', 'hora', 'monto')
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('medico', 'cita')
        return queryset

admin.site.site_header = 'Administracion de Centro Medico'
admin.site.site_title = 'Centro Medico'