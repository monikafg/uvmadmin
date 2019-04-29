from django import forms
from .models import Organizador

class OrganizadorForm(forms.ModelForm):

    class Meta:
        model = Organizador
        fields = ('tipo_organizador', 'nombre', 'web', 'logo')

        widgets = {
            'tipo_organizador': forms.Select(attrs={'class': 'form-control mb-2'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
                'placeholder': 'Nombre...', 'required': True
			}),
            'web': forms.URLInput(attrs={'class': 'form-control input-lg mb-2'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-2'}),
        }