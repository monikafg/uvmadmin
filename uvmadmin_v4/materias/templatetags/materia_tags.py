from django import template
from materias.models import Apunte, Ponencia

register = template.Library()

# Devuelve un query con todos los apuntes de la materia
@register.simple_tag
def get_apuntes_list(id_materia):
    return Apunte.objects.filter(materia=id_materia)

# Devuelve un query con todos las ponencias de la materia
@register.simple_tag
def get_ponencias_list(id_materia):
    return Ponencia.objects.filter(materia=id_materia)