# Para el manejo de formularios de Django y de Users
from django import forms    
from django.contrib.auth.forms import UserCreationForm
# Para manejar las vistas genéricas de Django
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
# Decoradores para controlar el acceso de los usuarios a las vistas
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
# Importamos los modelos y los formularios de la app
from .models import Profile   
from .forms import ProfileForm, EmailForm, UserCreationFormWithMail    

#====== Mixin requerirá que el usuario sea miembro del staff ========#
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

#========== Crear Nuevo Registro =============#
@method_decorator(staff_member_required, name='dispatch')
class SignUpView(CreateView):
    form_class = UserCreationFormWithMail    
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        # Cogemos el formulario general de SigUpView
        form = super(SignUpView, self).get_form()
        # Modificamos el formulario en tiempo real 
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        # Devolvemos el formulario modificado
        return form

#======= Actualizar Perfil Usuario Activo =========#
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

#==== Para Restaurar la Contraseña Usuario Activo ======#
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form

