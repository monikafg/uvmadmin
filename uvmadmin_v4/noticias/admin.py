from django.contrib import admin
from .models import Noticia

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }


admin.site.register(Noticia, NoticiaAdmin)

