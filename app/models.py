from django.db import models
from django.contrib.auth.models import User


class Medico(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    especialidad = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.nombre

class Cita(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

class Recaudacion(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    concepto = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f"Cita: {self.cita}, Monto: {self.monto}"
     
     

    def __str__(self):
        return self.concepto

