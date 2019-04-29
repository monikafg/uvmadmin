from django.db import models
from django.contrib.auth.models import User     # Para relacionar con Users de Django
from core.models import Edicion                 # Para relacionar con la Ediciones


# ------------------------------------------------------------------------
#  Modelo: Tipo_Organizador
# ------------------------------------------------------------------------
class Tipo_Organizador(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tipo_organizador"
        verbose_name_plural = "tipos_organizadores"
        ordering = ['descripcion']

    def __str__(self):        
        return self.descripcion

# ------------------------------------------------------------------------
#  Modelo: Organizador
#  Descripción: Organizadores, Patrocinadores y Colaboradores
# ------------------------------------------------------------------------
class Organizador(models.Model):
    # Enlaces con otros modelos
    edicion = models.ForeignKey(Edicion,verbose_name="Edicion", on_delete=models.CASCADE, default=18)
    tipo_organizador = models.ForeignKey(Tipo_Organizador,verbose_name="Tipo", on_delete=models.CASCADE)
    #Campos    
    nombre = models.CharField(max_length=100, verbose_name="Descripción")
    logo = models.ImageField(upload_to='core/logos', null=True, blank=True)
    web = models.URLField(verbose_name="Web", null=True, blank=True)
    # Campos de control
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "organizador"
        verbose_name_plural = "organizadores"
        ordering = ['tipo_organizador', 'nombre']

    def __str__(self):
        return self.nombre    


    def get_Organizadores_Tipo(self):
        return Organizador.objects.filter(tipo_organizador=self.tipo_organizador)
