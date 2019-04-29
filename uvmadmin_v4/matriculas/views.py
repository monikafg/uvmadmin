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
from .models import Matricula
from .forms import MatriculaForm
 
#============= Listado de Alumnos ==============#
@method_decorator(login_required, name='dispatch')
class MatriculaListView(ListView):
    model = Matricula

#============ Detalle de una noticia =============#
@method_decorator(login_required, name='dispatch')
class MatriculaDetailView(DetailView):
    model = Matricula
 
#============ Crear una nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class MatriculaCreate(CreateView):
    model = Matricula
    form_class = MatriculaForm
    success_url = reverse_lazy('matriculas:matriculas')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#============ Actualizar nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class MatriculaUpdate(UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('matriculas:matricula', args=[self.object.id]) 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#============ Eliminar nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class MatriculaDelete(DeleteView):
    model = Matricula
    success_url = reverse_lazy('matriculas:matriculas')