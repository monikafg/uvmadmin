from django import template
#from alumnos.models import Pais, Provincia, Municipio, Actividad
from matriculas.models import Matricula
from materias.models import Materia, Ponencia

register = template.Library()

# Devuelve un query con todas los municipios de la provincia indicada
@register.simple_tag
def get_alumno_matriculas(id_alumno=0):
    return Matricula.objects.filter(alumno=id_alumno)

@register.simple_tag
def get_ponente_materias(id_ponente=0, id_tipomateria=0):
    return Materia.objects.filter(ponente=id_ponente, tipo_materia=id_tipomateria)

@register.simple_tag
def get_ponente_ponencias(id_ponente=0):
    return Ponencia.objects.filter(ponente=id_ponente)