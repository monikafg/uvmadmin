from django.db import models
from django.utils.timezone import now                           # Para acceder a la fecha/hora actual
from djchoices import DjangoChoices, ChoiceItem

# ------------------------------------------------------------------------
#  Modelo: TipoDocumento
#  Descripción: Tipos de documentos de identidad (Nif, Nie, Cif, Pasaporte)
# ------------------------------------------------------------------------
class TipoDocumento(models.Model):    
    des_documento = models.CharField(max_length=100, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"
        ordering = ['-created']
        #db_table = 'tipo_documento'

    def __str__(self):
        return self.des_documento

# ------------------------------------------------------------------------
#  Modelo: Actividad
#  Descripción: Almacena distintas actividades profesionales
# ------------------------------------------------------------------------
class Actividad(models.Model):
    des_actividad = models.CharField(max_length=100, verbose_name="Descripción")
    id_descuento = models.IntegerField(verbose_name="Descuento", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "actividad"
        verbose_name_plural = "actividades"
        ordering = ['des_actividad']
        #db_table = 'actividad'

    def __str__(self):
        return self.des_actividad


# ------------------------------------------------------------------------
#  Modelo: Pais
#  Descripción: Paises
# ------------------------------------------------------------------------
class Pais(models.Model):
    cod_pais = models.CharField(max_length=2, verbose_name="Código")
    des_pais = models.CharField(max_length=100, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "pais"
        verbose_name_plural = "paises"
        ordering = ['des_pais']
        #db_table = 'pais'

    def __str__(self):
        return self.des_pais

# ------------------------------------------------------------------------
#  Modelo: Provincia
#  Descripción: Provicias de España
# ------------------------------------------------------------------------
class Provincia(models.Model):
    des_provincia = models.CharField(max_length=100, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "provincia"
        verbose_name_plural = "provincias"
        ordering = ['des_provincia']
        #db_table = 'provincia'

    def __str__(self):
        return self.des_provincia

# ------------------------------------------------------------------------
#  Modelo: Municipio
#  Descripción: Municipios de las provincias de España
# ------------------------------------------------------------------------
class Municipio(models.Model):    
    cod_provincia = models.ForeignKey(Provincia, verbose_name="Provincia", on_delete=models.CASCADE)
    cod_municipio = models.SmallIntegerField(verbose_name="Código Municipio")
    des_municipio = models.CharField(max_length=100, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "municipio"
        verbose_name_plural = "municipio"
        ordering = ['des_municipio']
        unique_together = (('cod_provincia', 'cod_municipio'),)
        #db_table = 'municipio'

    def __str__(self):
        return self.des_municipio

# ------------------------------------------------------------------------
#  Modelo: Alumno
#  Descripción: Todas alumnos matriculados
# ------------------------------------------------------------------------
class Alumno(models.Model):
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
    # Campos específicos para Alumnos
    actividad = models.ForeignKey(Actividad, verbose_name="Actividad", on_delete=models.CASCADE)
    recibirmail = models.BooleanField(default=False, verbose_name='Recibir Mail')
    # Fin Campos específicos para Alumnos
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "alumno"
        verbose_name_plural = "alumnos"
        ordering = ['-created']
        db_table = 'alumnos_alumno'
        
    def __str__(self):
        cadena = self.documento  + " - " + self.nombre + " " + self.apellido1 + " " + self.apellido2
        return cadena

    def get_fullname(self):
        return "%s %s %s" % (self.nombre, self.apellido1, self.apellido2)
