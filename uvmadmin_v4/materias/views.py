# Para manejar las vistas genéricas de Django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Para controlar el acceso de usuarios a las vistas
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
# Para los formularios modales
from bootstrap_modal_forms.generic import (BSModalUpdateView, BSModalDeleteView, BSModalCreateView)
# Importamos los modelos y los formularios de la app
from .models import Materia, Apunte, Ponencia
from .forms import (MateriaForm, MateriaUpdateForm, 
                    MateriaPonentesUpdateForm, MateriaApuntesForm, MateriaPonenciaForm)

#============= Listado de Noticias ==============#
@method_decorator(login_required, name='dispatch')
class MateriaListView(ListView):
    model = Materia

#============ Detalle de una noticia =============#
@method_decorator(login_required, name='dispatch')
class MateriaDetailView(DetailView):
    model = Materia
 
#============ Crear una nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class MateriaCreate(CreateView):
    model = Materia
    form_class = MateriaForm
    success_url = reverse_lazy('materias:materias')

#============ Actualizar nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class MateriaUpdate(UpdateView):
    model = Materia
    form_class = MateriaUpdateForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('materias:editar', args=[self.object.id]) + '?ok'

#============ Eliminar nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class MateriaDelete(DeleteView):
    model = Materia
    success_url = reverse_lazy('materias:materias')

#============ Actualizar Ponentes =============#
@method_decorator(login_required, name='dispatch')
class MateriaPonentesUpdate(BSModalUpdateView):
    model = Materia
    template_name = 'materias/ponentes/materia_ponentes_form.html'
    form_class = MateriaPonentesUpdateForm
    success_message = 'Success: Ponente añadido con éxito.'
 
    def get_success_url(self):
        return reverse_lazy('materias:editar', args=[self.object.id]) 

#============ Añadir Apuntes =============#
@method_decorator(login_required, name='dispatch')
class MateriaApuntesCreate(BSModalCreateView):
    model = Materia
    template_name = 'materias/apuntes/materia_apuntes_add.html'
    form_class = MateriaApuntesForm
    success_message = 'Success: Apuntes añadido con éxito.'
 
    def get_success_url(self):
        return reverse_lazy('materias:materia', args=[self.kwargs['pk']]) 

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.materia = Materia.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

#============ Actualizar Apuntes =============#
class MateriaApuntesUpdate(BSModalUpdateView):
    model = Apunte
    template_name = 'materias/apuntes/materia_apuntes_upd.html'
    form_class = MateriaApuntesForm
    success_message = 'Success: Apuntes Actualizados'

    def get_success_url(self):
        return reverse_lazy('materias:materia', args=[self.kwargs['mat']]) 


#============ Eliminar Apuntes =============#
class MateriaApuntesDelete(BSModalDeleteView):    
    model = Apunte
    template_name = 'materias/apuntes/materia_apuntes_del.html'
    success_message = 'Success: Los Apuntes se han eliminado.'

    def get_success_url(self):
        return reverse_lazy('materias:materia', args=[self.kwargs['mat']]) 

#============ Añadir Ponencia =============#
@method_decorator(login_required, name='dispatch')
class MateriaPonenciaCreate(BSModalCreateView):
    model = Materia
    template_name = 'materias/ponencias/materia_ponencia_add.html'
    form_class = MateriaPonenciaForm
    success_message = 'Success: Ponencia añadida con éxito.'
 
    def get_success_url(self):
        return reverse_lazy('materias:materia', args=[self.kwargs['pk']]) 

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.materia = Materia.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

#============ Actualizar Ponencia =============#
class MateriaPonenciaUpdate(BSModalUpdateView):
    model = Ponencia
    template_name = 'materias/ponencias/materia_ponencia_upd.html'
    form_class = MateriaPonenciaForm
    success_message = 'Success: Ponencia Actualizada'

    def get_success_url(self):
        return reverse_lazy('materias:materia', args=[self.kwargs['mat']]) 


#============ Eliminar Ponencia =============#
class MateriaPonenciaDelete(BSModalDeleteView):
    model = Ponencia
    template_name = 'materias/ponencias/materia_ponencia_del.html'
    success_message = 'Success: La Ponencia se han eliminado.'

    def get_success_url(self):
        return reverse_lazy('materias:materia', args=[self.kwargs['mat']]) 