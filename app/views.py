"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Cita, Medico, Recaudacion
from .forms import RecaudacionForm
from django.views.generic import ListView
from django.contrib import messages

def recaudaciones_medico(request, medico_id):
    medico = Medico.objects.get(id=medico_id)
    recaudaciones = Recaudacion.objects.filter(medico=medico)
    return render(request, 'app/recaudaciones_medico.html', {'medico': medico, 'recaudaciones': recaudaciones})

def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'app/medicos.html', {'medicos': medicos})

def citas_medico(request, medico_id):
    medico = Medico.objects.get(id=medico_id)
    citas = Cita.objects.filter(medico=medico)
    return render(request, 'app/citas.html', {'citas': citas})

def ingresar_recaudacion(request, medico_id):
    medico = Medico.objects.get(id=medico_id)

    if request.method == 'POST':
        form = RecaudacionForm(request.POST)
        if form.is_valid():
            recaudacion = form.save(commit=False)
            recaudacion.medico = medico
            recaudacion.save()
            
            messages.success(request, 'Recaudacion ingresada')
            return redirect('ingresar_recaudacion', medico_id=medico_id)
    else:
        form = RecaudacionForm()

    return render(request, 'app/ingresar_recaudacion.html', {'form': form, 'medico': medico})

class RecaudacionListView(ListView):
    model = Recaudacion
    template_name = 'app/recaudaciones_medico.html'
    context_object_name = 'recaudaciones'

    def get_queryset(self):
        medico_id = self.kwargs['medico_id']
        return Recaudacion.objects.filter(medico_id=medico_id)

class MedicoListView(ListView):
    model = Medico
    template_name = 'app/medicos.html'
    context_object_name = 'medicos'

def reservar_cita(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        medico_id = request.POST['medico']
        medico = Medico.objects.get(pk=medico_id)
        cita = Cita(nombre=nombre, fecha=fecha, hora=hora, medico=medico)
        cita.save()
        
        messages.success(request, 'Cita reservada')
        return redirect('reservar_cita')

    medicos = Medico.objects.all()
    return render(request, 'app/reservar_cita.html', {'medicos': medicos})


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
