
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Recaudacion, Cita, Medico

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RecaudacionForm(forms.ModelForm):
    class Meta:
        model = Recaudacion
        fields = ['concepto', 'monto', 'medico', 'cita', 'fecha', 'hora']
        exclude = ['medico']

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre', 'medico', 'fecha', 'hora']


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'especialidad']