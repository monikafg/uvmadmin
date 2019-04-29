from django.db import models                    # Para trabajar con modelos
from django.utils.timezone import now           # Para coger la fecha actual
from django.contrib.auth.models import User     # Para relacionar con Users de Django
from materias.models import Materia             # Para relacionar la matrícula con la materia
from alumnos.models import Alumno               # Para relacionar la matrícula con el alumno
from core.models import Edicion                 # Para relacionar la matrícula con el alumno

# ------------------------------------------------------------------------
#  Modelo: Lugar
#  Descripción: Lugares de Pago
# ------------------------------------------------------------------------
class Lugar(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name="Lugar de Pago")
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "lugar"
        verbose_name_plural = "lugares"
        ordering = ['descripcion']

    def __str__(self):        
        return self.descripcion

# ------------------------------------------------------------------------
#  Modelo: Estado
#  Descripción: Estado Matrícula
# ------------------------------------------------------------------------
class Estado(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "estados"
        ordering = ['descripcion']

    def __str__(self):        
        return self.descripcion

# ------------------------------------------------------------------------
#  Modelo: Matricula
#  Descripción: Matrículas de los alumnos
# ------------------------------------------------------------------------
class Matricula(models.Model):
    # Enlaces con otros modelos
    edicion = models.ForeignKey(Edicion,verbose_name="Edicion", on_delete=models.CASCADE, default=18)
    materia = models.ForeignKey(Materia,verbose_name="Materias", on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, verbose_name="Alumnos", on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar,verbose_name="Lugar Pago", on_delete=models.CASCADE, null=True, blank=True)
    estado = models.ForeignKey(Estado,verbose_name="Estado", on_delete=models.CASCADE, default=1)
    #Campos    
    freserva = models.DateField(verbose_name="Fecha Reserva", null=True, blank=True, default=now)
    fpago = models.DateField(verbose_name="Fecha Pago", null=True, blank=True)    
    impreso = models.BooleanField(verbose_name="Impreso", default=False)
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
 
    class Meta:
        verbose_name = "matricula"
        verbose_name_plural = "matriculas"
        ordering = ['-created']

    def __str__(self):
        return "(" + str(self.id).zfill(4) + ") " + self.alumno.get_fullname()

    def get_matriculas_alumno(self):
        return Matricula.objects.filter(alumno=self.alumno.id)

    def get_matriculas_materia(self):
        return Matricula.objects.filter(materia=self.materia.id)
    
    def get_descuento(self):
        actividad = self.alumno.actividad.id_descuento
        descuentos = self.materia.descuento.get(id=actividad)
        return descuentos

