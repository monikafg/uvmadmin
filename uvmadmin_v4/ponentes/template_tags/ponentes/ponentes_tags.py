from django import template
from materias.models import Materia

register = template.Library()

# Devuelve los cursos o talleres de un ponente
@register.simple_tag
def get_ponente_materias(id_ponente=0, id_tipomateria=0):
    return Materia.objects.filter(ponente=id_ponente, tipo_materia=id_tipomateria)
