# Para manejar las vistas genéricas de Django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
# Para controlar el acceso de usuarios a las vistas
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Importamos los modelos y los formularios de la app
from .models import Alumno
from .forms import AlumnoForm
 
#============= Listado de Alumnos ==============#
@method_decorator(login_required, name='dispatch')
class AlumnoListView(ListView):
    model = Alumno
    
#============ Detalle de un Alumno =============#
@method_decorator(login_required, name='dispatch')
class AlumnoDetailView(DetailView):
    template_name = "alumnos/alumno_detail.html"
    model = Alumno

#============ Crear nuevo Alumno =============#
@method_decorator(login_required, name='dispatch')
class AlumnoCreate(CreateView):
    model = Alumno
    form_class = AlumnoForm
    success_url = reverse_lazy('alumnos:alumnos')
 
#============ Actualizar Alumno =============#
@method_decorator(login_required, name='dispatch')
class AlumnoUpdate(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('alumnos:editar', args=[self.object.id]) + '?ok'

#============ Eliminar nuevo Alumno =============#
@method_decorator(login_required, name='dispatch')
class AlumnoDelete(DeleteView):
    model = Alumno
    success_url = reverse_lazy('alumnos:alumnos')