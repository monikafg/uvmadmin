"""uvmadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# URLs de las App Propias
from core.urls import core_patterns       
from noticias.urls import noticias_patterns     
from alumnos.urls import alumnos_patterns  
from ponentes.urls import ponentes_patterns
from materias.urls import materias_patterns
from matriculas.urls import matriculas_patterns
from pages.urls import pages_patterns
from universidad.urls import universidad_patterns
      
# Para poder ver imágenes en desarrollo (fichero static). Ver abajo del todo
from django.conf import settings

urlpatterns = [
    # Paths de las App propias
    path('', include(core_patterns)),
    path('noticias/', include(noticias_patterns)),
    path('alumnos/', include(alumnos_patterns)),
    path('materias/', include(materias_patterns)),
    path('ponentes/', include(ponentes_patterns)),
    path('matriculas/', include(matriculas_patterns)),
    path('paginas/', include(pages_patterns)),
    path('universidad/', include(universidad_patterns)),
    # Paths de terceros
    path('galeria/', include('gallery.urls')),
    # Paths del admin
    path('admin/', admin.site.urls),
    # Paths de Auth (Autenticación)
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),        # Aumentamos las listas de posibles paths de accounts
]

# Para poder ver imágenes en desarrollo (fichero static)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)