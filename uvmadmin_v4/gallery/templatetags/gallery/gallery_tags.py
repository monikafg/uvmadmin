from django import template
from gallery.models import Album

register = template.Library()

# Devuelve todos los álbumes
@register.simple_tag
def get_album_list():
    return Album.objects.all()
