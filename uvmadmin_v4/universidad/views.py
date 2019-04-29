# Para manejar las vistas genéricas de Django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Para controlar el acceso de usuarios a las vistas
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
# Importamos los modelos y los formularios de la ap
from .models import Organizador
from .forms import OrganizadorForm

#============= Listado de Noticias ==============#
@method_decorator(login_required, name='dispatch')
class OrganizadorListView(ListView):
    model = Organizador

#============ Detalle de una noticia =============#
@method_decorator(login_required, name='dispatch')
class OrganizadorDetailView(DetailView):
    model = Organizador
 
#============ Crear una nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class OrganizadorCreate(CreateView):
    model = Organizador
    form_class = OrganizadorForm
    success_url = reverse_lazy('universidad:organizadores')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
 
#============ Actualizar nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class OrganizadorUpdate(UpdateView):
    model = Organizador
    form_class = OrganizadorForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('universidad:organizador', args=[self.object.id, slugify(self.object.nombre)]) 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#============ Eliminar nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class OrganizadorDelete(DeleteView):
    model = Organizador
    success_url = reverse_lazy('universidad:organizadores')
