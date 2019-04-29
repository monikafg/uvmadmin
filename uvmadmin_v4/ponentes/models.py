from django.db import models                        # Para trabajar con modelos
from django.utils.timezone import now               # Para coger la fecha actual
from djchoices import DjangoChoices, ChoiceItem     # Para poder hacer opciones
from ckeditor.fields import RichTextField           # Para incluir el editor de texto CKEditor
from alumnos.models import TipoDocumento, Pais, Provincia

# ------------------------------------------------------------------------
#  Modelo: Ponente
#  Descripción: Todos los ponentes
# ------------------------------------------------------------------------
class Ponente(models.Model):
    # Choices
    TIPO_GENERO = (("M", "Masculino"), ("F", "Femenino"), )
    # Campos
    tipo_documento = models.ForeignKey(TipoDocumento,verbose_name="Tipo Documento", on_delete=models.CASCADE)
    documento = models.CharField(max_length=20,  unique=True, verbose_name="Documento")        
    nombre = models.CharField(max_length=20, verbose_name="Nombre")        
    apellido1 = models.CharField(max_length=20, verbose_name="Primer Apellido")        
    apellido2 = models.CharField(max_length=20, verbose_name="Segundo Apellido")        
    pais = models.ForeignKey(Pais, verbose_name="Pais", on_delete=models.CASCADE, default=51)
    provincia = models.ForeignKey(Provincia, verbose_name="Provincia", on_delete=models.CASCADE, default=35)
    des_municipio = models.CharField(max_length=100, verbose_name="Municipio", default="")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")        
    cod_postal = models.CharField(max_length=10, verbose_name="Código Postal", null=True, blank=True)        
    telefono1 = models.CharField(max_length=20, verbose_name="Teléfono 1")        
    telefono2 = models.CharField(max_length=20, verbose_name="Teléfono 2", null=True, blank=True)        
    email1 = models.EmailField(max_length=100, verbose_name="Correo Electrónico 1")
    email2 = models.EmailField(max_length=100, verbose_name="Correo Electrónico 2", null=True, blank=True)
    nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=True, blank=True)
    genero = models.CharField(max_length=1, choices=TIPO_GENERO, verbose_name='Genero')
    foto = models.ImageField(verbose_name="Foto", upload_to="personas", null=True, blank=True)
    residente = models.BooleanField(default=False, verbose_name="Residente")
    # Campos específicos para Ponentes
    cargo = RichTextField(verbose_name="Contenido")
    curriculum = models.FileField(verbose_name="Curriculum Vitae", upload_to='ponentes', null=True, blank=True)
    web = models.URLField(verbose_name="Web", null=True, blank=True)
    # Fin Campos específicos para Ponentes
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "ponente"
        verbose_name_plural = "ponentes"
        ordering = ['-created']

    def __str__(self):
        cadena = self.documento  + " - " + self.nombre + " " + self.apellido1 + " " + self.apellido2
        return cadena

    def get_fullname(self):
        return "%s %s %s" % (self.nombre, self.apellido1, self.apellido2)
