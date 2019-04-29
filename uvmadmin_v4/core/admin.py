from django.contrib import admin
from .models import Edicion

# Register your models here.
class EdicionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'des_edicion', 'edicion', 'activa')



# Registramos en el sitio del administrador las clases definidas
admin.site.register(Edicion, EdicionAdmin)


