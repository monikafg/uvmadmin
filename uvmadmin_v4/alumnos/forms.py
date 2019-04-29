from django import forms
from .models import Alumno

#================================================================
# Formulario: AlumnoForm
# Modelos: Alumno.
#================================================================
class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = fields = '__all__'
        
        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-control mb-2'}),
			'documento': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
                'placeholder': 'Documento...', 'required': True
			}),
			'nombre': forms.TextInput(attrs={'class': 'form-control input-lg mt-2 mb-2',
                'placeholder': 'Nombre...', 'required': True
			}),
			'apellido1': forms.TextInput(attrs={'class': 'form-control input-lg mt-2 mb-2',
                'placeholder': 'Primer Apellido...', 'required': True
			}),
			'apellido2': forms.TextInput(attrs={'class': 'form-control input-lg mt-2 mb-2',
                'placeholder': 'Segundo Apellido...', 'required': True
			}),
            'pais': forms.Select(attrs={'class': 'form-control mb-2'}),
            'provincia': forms.Select(attrs={'class': 'form-control mb-2'}),
            'municipio': forms.Select(attrs={'class': 'form-control mb-2'}),
			'des_municipio': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
                'placeholder': 'Municipio...'
			}),
			'direccion': forms.TextInput(attrs={'class': 'form-control input-lg mt-2 mb-2',
                'placeholder': 'Dirección...'
			}),
			'cod_postal': forms.NumberInput(attrs={'class': 'form-control input-lg mb-2'}),
			'telefono1': forms.TextInput(attrs={'class': 'form-control input-lg mt-2 mb-2',
                'placeholder': 'Teléfono 1...'
			}),
			'telefono2': forms.TextInput(attrs={'class': 'form-control input-lg mt-2 mb-2',
                'placeholder': 'Teléfono 2...'
			}),
			'email1': forms.EmailInput(attrs={'class': 'form-control input-lg mt-2 mb-2',
                'placeholder': 'Correo electrónico 1...'
			}),
			'email2': forms.EmailInput(attrs={'class': 'form-control input-lg mt-2 mb-2',
                'placeholder': 'Correo electrónico 2...'
			}),
            'genero': forms.Select(attrs={'class': 'form-control mb-2', 'required': True}),
            'residente': forms.Select(attrs={'class': 'form-control ml-2 mt-2', 'required': True},choices=((False, 'No Residente'), (True, 'Residente'))),
            # Campos exclusivos de Alumnos
            'actividad': forms.Select(attrs={'class': 'form-control mb-2', 'required': True}),
            'recibirmail': forms.Select(attrs={'class': 'form-control ml-2 mt-2', 'required': True},choices=((False, 'No Enviar Mail'), (True, 'Si Enviar Mail'))),
            # Fin Campos exclusivos de Alumnos
			'nacimiento': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'date',}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-2'}),
        }


