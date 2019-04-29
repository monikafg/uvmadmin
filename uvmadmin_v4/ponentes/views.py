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
from .models import Ponente
from .forms import PonenteForm, PonenteUpdateForm
 
#============= Listado de Ponentes ==============#
@method_decorator(login_required, name='dispatch')
class PonenteListView(ListView):
    model = Ponente
    
#============ Detalle de un Ponente =============#
@method_decorator(login_required, name='dispatch')
class PonenteDetailView(DetailView):
    template_name = "ponentes/ponente_detail.html"
    model = Ponente

#============ Crear nuevo Ponente =============#
@method_decorator(login_required, name='dispatch')
class PonenteCreate(CreateView):
    model = Ponente
    form_class = PonenteForm
    success_url = reverse_lazy('ponentes:ponentes')
 
#============ Actualizar Ponente =============#
@method_decorator(login_required, name='dispatch')
class PonenteUpdate(UpdateView):
    model = Ponente
    form_class = PonenteUpdateForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ponentes:editar', args=[self.object.id]) + '?ok'

#============ Eliminar nuevo Ponente =============#
@method_decorator(login_required, name='dispatch')
class PonenteDelete(DeleteView):
    model = Ponente
    success_url = reverse_lazy('ponentes:ponentes')