from django.db import models                    # Para trabajar con modelos
from django.utils.timezone import now           # Para coger la fecha actual
from django.contrib.auth.models import User     # Para relacionar con Users de Django
from ckeditor.fields import RichTextField       # Para incluir el editor de texto CKEditor
from core.models import Edicion                 # Para relacionar la materia con la edición
from ponentes.models import Ponente             # Para relacionar la ponencia con los ponentes


# ------------------------------------------------------------------------
#  Modelo: Descuento
#  Descripción: Descuentos aplicables a las materias
# ------------------------------------------------------------------------
class Descuento(models.Model):    
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    importe = models.DecimalField(verbose_name="Importe", max_digits=10, decimal_places=2, default=25)
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "descuento"
        verbose_name_plural = "descuentos"
        ordering = ['id']

    def __str__(self):
        cadena=self.descripcion + " ("+str(self.importe)+"€)"
        return cadena

# ------------------------------------------------------------------------
#  Modelo: TipoMateria
#  Descripción: Tipos de materias ('Curso', 'Taller'...)
# ------------------------------------------------------------------------
class TipoMateria(models.Model):    
    des_materia = models.CharField(max_length=100, verbose_name="Descripción")
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tipomateria"
        verbose_name_plural = "tiposmaterias"
        ordering = ['-created']

    def __str__(self):
        return self.des_materia

# ------------------------------------------------------------------------
#  Modelo: Materia
#  Descripción: Datos de los cursos y talleres
# ------------------------------------------------------------------------
class Materia(models.Model): 
    # Texto para cuenta
    TEXTO_CC = "Ir al enlace que aparece en la información del curso para REGISTRARSE y PAGAR. (Cada curso se abona de forma individual)."

    # Enlaces con otros modelos
    tipo_materia = models.ForeignKey(TipoMateria,verbose_name="Tipo Materia", on_delete=models.CASCADE)
    edicion = models.ForeignKey(Edicion,verbose_name="Edición", on_delete=models.CASCADE, default=18)
    ponente = models.ManyToManyField(Ponente, blank=True, verbose_name="Ponentes")
    descuento = models.ManyToManyField(Descuento, blank=True, verbose_name="Descuentos")
    # Campos
    codigo = models.CharField(verbose_name="Código", max_length=4)
    denominacion = models.CharField(verbose_name="Denominacion", max_length=200)
    lugar = models.CharField(verbose_name="Lugar Celebración", max_length=200, default="")
    descripcion = RichTextField(verbose_name="Descripcion")
    imagen = models.ImageField(upload_to='materias/imagenes', null=True, blank=True)
    programa = models.FileField(upload_to='materias/programas', null=True, blank=True)
    finicio = models.DateField(verbose_name="Fecha inicio", null=True, blank=True)
    ffin = models.DateField(verbose_name="Fecha fin", null=True, blank=True)
    hinicio = models.TimeField(verbose_name="Hora inicio", null=True, blank=True)
    hfin = models.TimeField(verbose_name="Hora fin", null=True, blank=True)
    creditos = models.DecimalField(verbose_name="Créditos", max_digits=3, decimal_places=1, default=0)
    horas = models.SmallIntegerField(verbose_name="Horas", default=0)
    observaciones = RichTextField(verbose_name="Observaciones")
    importe = models.DecimalField(verbose_name="Importe Normal", max_digits=10, decimal_places=2, default=0)
    importe_reducido = models.DecimalField(verbose_name="Importe Reducido", max_digits=10, decimal_places=2, default=0)
    plazas = models.SmallIntegerField(verbose_name="Plazas", default=0)
    aplica_dto = models.BooleanField(verbose_name="Aplica Descuento", default=False)
    plazas_dto = models.SmallIntegerField(verbose_name="Plazas con Descuento", default=0)
    plazas_dto_ocupadas = models.SmallIntegerField(verbose_name="Plazas con Descuento Ocupadas", default=0)
    otracuenta = models.BooleanField(verbose_name="Otro Número de Cuenta", default=False)
    cuenta = models.CharField(verbose_name="Cuenta", max_length=200, default=TEXTO_CC)
    activo = models.BooleanField(verbose_name="Activo", default=False)
    dirigido = models.CharField(verbose_name="Dirigido a", max_length=200, default="Todos los públicos")
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"
        ordering = ['-created']

    def __str__(self):
        return self.denominacion

    def get_fullname(self):
        return '%s - %s' % (self.codigo, self.denominacion)

# ------------------------------------------------------------------------
#  Modelo: Apuntes
#  Descripción: Apuntes de la materia
# ------------------------------------------------------------------------
class Apunte(models.Model):
    # Enlaces con otros modelos
    materia = models.ForeignKey(Materia, verbose_name="Materia", on_delete=models.CASCADE)
    # Campos
    des_apunte = models.CharField(max_length=100, verbose_name="Descripción")
    fichero = models.FileField(upload_to='materias/apuntes', null=True, blank=True)
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "apunte"
        verbose_name_plural = "apuntes"
        ordering = ['-created']

    def __str__(self):
        return self.des_apunte


# ------------------------------------------------------------------------
#  Modelo: Ponencia
#  Descripción: Datos de las ponencias de las materias
# ------------------------------------------------------------------------
class Ponencia(models.Model):
    # Enlaces con otros modelos
    materia = models.ForeignKey(Materia,verbose_name="Materia", on_delete=models.CASCADE)
    ponente = models.ManyToManyField(Ponente, blank=True, verbose_name="Ponentes")
    #Campos    
    denominacion = models.CharField(verbose_name="Denominacion", max_length=200)
    fecha = models.DateField(verbose_name="Fecha", null=True, blank=True)
    hinicio = models.TimeField(verbose_name="Hora Inicio", null=True, blank=True)
    hfin = models.TimeField(verbose_name="Hora Fin", null=True, blank=True)
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
 
    class Meta:
        verbose_name = "ponencia"
        verbose_name_plural = "ponencias"
        ordering = ['materia', 'denominacion']

    def __str__(self):
        return self.denominacion