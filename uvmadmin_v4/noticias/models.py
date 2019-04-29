from django.db import models                    # Para trabajar con modelos
from django.utils.timezone import now           # Para coger la fecha actual
from django.contrib.auth.models import User     # Para relacionar con Users de Django
from gallery.models import Album                # Para enlazar la Noticia con un álbum de fotos
from ckeditor.fields import RichTextField       # Para incluir el editor de texto CKEditor

DEFAULT_USER_ID = 2
class Noticia(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    subject = models.CharField(verbose_name="Entradilla", max_length=200, default="")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='noticias', null=True, blank=True)
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    author = models.ForeignKey(User, verbose_name="Autor", default=DEFAULT_USER_ID,  on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    galeria = models.ForeignKey(Album, verbose_name="Galeria", null=True, blank=True, on_delete=models.SET_NULL) 
    fichero = models.FileField(upload_to='noticias', null=True, blank=True)

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['-created', 'title']

    def __str__(self):
        return self.title

    
