from django.contrib import admin
from .models import Matricula, Lugar, Estado

# Register your models here.
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'materia', 'alumno', 'estado')

class LugarAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')


admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Estado, EstadoAdmin)
