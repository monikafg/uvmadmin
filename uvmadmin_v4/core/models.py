from django.db import models
from django.utils.timezone import now           # Para acceder a la fecha/hora actual

# ------------------------------------------------------------------------
#  Modelo: Edicion
#  Descripción: Ediciones de la Universidad de Verano de Maspalomas
# ------------------------------------------------------------------------
class Edicion(models.Model):
    des_edicion = models.CharField(max_length=100, verbose_name="Descripción")
    edicion = models.SmallIntegerField(default=0, verbose_name="Año Edición")
    activa = models.BooleanField(default=False, verbose_name="Edición Activa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "edicion"
        verbose_name_plural = "ediciones"
        ordering = ['-created']

    def __str__(self):
        return self.des_edicion
