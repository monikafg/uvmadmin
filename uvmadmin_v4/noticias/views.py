# Para manejar las vistas genéricas de Django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Para controlar el acceso de usuarios a las vistas
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
# Importamos los modelos y los formularios de la ap
from .models import Noticia
from .forms import NoticiaForm


#============= Mostrar un PDF ==============#
def pdfView(request):
    image_data = open('', 'rb').read()
    return HttpResponse(image_data, mimetype='application/pdf')


#============= Listado de Noticias ==============#
@method_decorator(login_required, name='dispatch')
class NoticiaListView(ListView):
    model = Noticia

#============ Detalle de una noticia =============#
@method_decorator(login_required, name='dispatch')
class NoticiaDetailView(DetailView):
    model = Noticia
 
#============ Crear una nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class NoticiaCreate(CreateView):
    model = Noticia
    form_class = NoticiaForm
    success_url = reverse_lazy('noticias:noticias')
 
#============ Actualizar nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class NoticiaUpdate(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('noticias:editar', args=[self.object.id]) + '?ok'

#============ Eliminar nueva noticia =============#
@method_decorator(login_required, name='dispatch')
class NoticiaDelete(DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:noticias')

