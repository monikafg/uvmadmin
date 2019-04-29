from django.contrib import admin
from .models import Actividad, Pais, Provincia, Municipio, TipoDocumento, Alumno

# Register your models here.
class ActividadAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'des_actividad')

class PaisAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'des_pais')

class ProvinciaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'des_provincia')

class MunicipioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'cod_provincia', 'cod_municipio', 'des_municipio')

class TipoDocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'des_documento')

class AlumnoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'documento', 'nombre', 'apellido1', 'apellido2')
 

# Registramos en el sitio del administrador las clases definidas
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Alumno, AlumnoAdmin)
