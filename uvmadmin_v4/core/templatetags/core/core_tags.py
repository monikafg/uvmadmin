from django import template
from core.models import Edicion
from alumnos.models import Alumno
from noticias.models import Noticia
from ponentes.models import Ponente
from materias.models import Materia
from matriculas.models import Matricula
from gallery.models import Album

register = template.Library()

# CONTADORES 
@register.simple_tag
def get_noticias_count():
    return Noticia.objects.count()

@register.simple_tag
def get_alumnos_count():
    return Alumno.objects.count()

@register.simple_tag
def get_ponentes_count():
    return Ponente.objects.count()

@register.simple_tag
def get_materias_count():
    return Materia.objects.count()

@register.simple_tag
def get_matriculas_count():
    return Matricula.objects.count()

@register.simple_tag
def get_galerias_count():
    return Album.objects.count()



# EDICIONES
@register.simple_tag
def get_edicion_list():
    return Edicion.objects.order_by('-edicion')

@register.simple_tag
def get_edicion_count():
    return Edicion.objects.count()

@register.simple_tag
def get_edicion_activa():
    return Edicion.objects.filter(activa=1)

# GALERÍA
@register.simple_tag
def get_galeria_noticias(id_galeria=0):
    return Noticia.objects.filter(galeria=id_galeria)
