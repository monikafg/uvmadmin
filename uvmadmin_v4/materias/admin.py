from django.contrib import admin
from .models import (Materia, TipoMateria, 
                    Ponencia, Apunte, Descuento)

# Register your models here.
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('tipo_materia', 'edicion', 'denominacion', 'activo')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

class TipoMateriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'des_materia')

class PonenciaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'materia', 'denominacion')

class ApunteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'materia', 'des_apunte')

class DescuentoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'descripcion', 'importe')

admin.site.register(Materia, MateriaAdmin)
admin.site.register(TipoMateria, TipoMateriaAdmin)
admin.site.register(Ponencia, PonenciaAdmin)
admin.site.register(Apunte, ApunteAdmin)
admin.site.register(Descuento, DescuentoAdmin)