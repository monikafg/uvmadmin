from django.apps import AppConfig

class GalleryConfig(AppConfig):
    name = 'gallery'
    verbose_name = 'Galerías de Fotos'

    def ready(self):
        import gallery.signals