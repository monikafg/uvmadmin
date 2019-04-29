from django.contrib import admin
from .models import Tipo_Organizador, Organizador
# Register your models here.

class Tipo_OrganizadorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'descripcion')

class OrganizadorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'nombre', 'web')

admin.site.register(Tipo_Organizador, Tipo_OrganizadorAdmin)
admin.site.register(Organizador, OrganizadorAdmin)