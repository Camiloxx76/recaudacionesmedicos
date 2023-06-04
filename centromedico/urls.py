"""
Definition of urls for centromedico.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views, forms
from app.views import MedicoListView

urlpatterns = [
    path('medicos/', MedicoListView.as_view(), name='medicos_list'),
    path('recaudaciones/<int:medico_id>/', views.recaudaciones_medico, name='recaudaciones_medico'),
    path('ingresar_recaudacion/<int:medico_id>/', views.ingresar_recaudacion, name='ingresar_recaudacion'),
    path('citas/<int:medico_id>/', views.citas_medico, name='citas_medico'),
    path('reservar/', views.reservar_cita, name='reservar_cita'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
   
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
