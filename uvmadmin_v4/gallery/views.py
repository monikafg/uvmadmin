# Para manejar las vistas genéricas de Django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
# Para controlar el acceso de usuarios a las vistas
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Mensaje y más cositas
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
# Modelos y Formularios necesarios
from gallery.models import Image, Album
from gallery.forms import AlbumForm


@method_decorator(login_required, name='dispatch')
class AlbumView(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        album = super(AlbumView, self).get_queryset()
        return album

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)
        images = context['album'].images.all()
        context['images'] = sorted(images, key=lambda i: i.date_taken)
        return context


@method_decorator(login_required, name='dispatch')
class AlbumList(ListView):
    model = Album
    template_name = 'gallery/album_list.html'

    def get_queryset(self):
        # Return a list of albums containing a highlight even if none is selected
        album_list = []
        for album in super(AlbumList, self).get_queryset().order_by('-pk'):
            # if there is no highlight but there are images in the album, use the first
            if not album.highlight and album.images.count():
                first_image = album.images.earliest('id')
                album.highlight = first_image
            album_list.append(album)
            if album.highlight:
                album.highlight.title = album.title  # override highlight title
        return album_list

#=====================================================
# Vista: AlbumCreate
#        Crea un nuevo album de fotos
#=====================================================
@method_decorator(login_required, name='dispatch')
class AlbumCreate(CreateView):
    model = Album
    form_class = AlbumForm

    def get_success_url(self):
        return reverse('gallery:album_list')

    def form_valid(self, form):
        # Salvamos el objeto
        self.object = form.save(commit=False)
        # Recuperamos en un array todas las imágenes seleccionadas
        image_data = form.files.getlist('imagenes')
        # Grabamos la nueva galería para poder acceder al id y grabar las imágenes
        self.object.save()
        # Recorremos todas las imágenes seleccionadas, creamos el objeto y lo añadimos al álbum
        for data in image_data:
            # Creamos el objeto imagen
            image = Image.objects.create(data=data)
            # Añadimos la imagen creada en la lista de imágenes de la galería
            form.instance.images.add(image)  

        return HttpResponseRedirect(self.get_success_url())

#=====================================================
# Vista: AlbumDelete
#        Elimina un álbum
#=====================================================
@method_decorator(login_required, name='dispatch')
class AlbumDelete(DeleteView):
    model = Album
    
    def get_success_url(self):
        return reverse('gallery:album_list')

#=====================================================
# Vista: AlbumUpdate
#        Elimina un álbum
#=====================================================
@method_decorator(login_required, name='dispatch')
class AlbumUpdate(UpdateView):

    model = Album
    form_class = AlbumForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('gallery:album_detail', args=[self.object.id, self.object.slug])
  
    def form_valid(self, form):
        # Recuperamos en un array todas las imágenes seleccionadas
        image_data = form.files.getlist('imagenes')
        # Recorremos todas las imágenes seleccionadas, creamos el objeto y lo añadimos al álbum
        for data in image_data:
            # Creamos el objeto imagen
            image = Image.objects.create(data=data)
            # Añadimos la imagen creada en la lista de imágenes de la galería
            form.instance.images.add(image)  
        return HttpResponseRedirect(self.get_success_url())