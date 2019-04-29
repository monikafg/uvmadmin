# Para manejar las vistas genéricas de Django
from django.views.generic.base import TemplateView

# Para controlar el acceso de usuarios a las vistas
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#============= Página Principal 'Home' ==============#
@method_decorator(login_required, name='dispatch')
class home(TemplateView):
    template_name = "core/home.html"
