from django import forms
from bootstrap_modal_forms.forms import BSModalForm 	# Formularios Modales

from .models import Materia, Apunte, Ponencia

class MateriaForm(forms.ModelForm):

    class Meta:
        model = Materia
        fields = '__all__'

        widgets = {
            'tipo_materia': forms.Select(attrs={'class': 'form-control mb-2'}),
            'edicion': forms.Select(attrs={'class': 'form-control mb-2'}),
			'codigo': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
                'placeholder': 'Código...', 'required': True
			}),
			'denominacion': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
                'placeholder': 'Denominación...', 'required': True
			}),
			# Solo en edición
            'ponente': forms.SelectMultiple(attrs={'class': 'form-control mb-2'}),
            'descuento': forms.SelectMultiple(attrs={'class': 'form-control mb-2'}),
			'lugar': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
				'placeholder': 'Lugar de Celebración...', 'required': True
			}),
			'descripcion': forms.Textarea(attrs={'class': 'form-control input-lg mb-2',
                'required': True
			}),
			'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-2'}),			
			'finicio': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'date',}),
			'hinicio': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'time',}),
			'ffin': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'date',}),
			'hfin': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'time',}),
			'programa': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-2'}),
			'dirigido': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
				'placeholder': 'Dirigido a...'
			}),
			'creditos': forms.NumberInput(attrs={'class': 'form-control mb-2', 'step':0.25, 'min':0, 'default':0}),
			'horas': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'default':0}),
			'importe': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'max':100.00, 'default':0}),
			# No sé si se calcula a parte
			'importe_reducido': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'max':100.00, 'default':0}),
			'plazas': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'default':0}),
            'aplica_dto': forms.Select(attrs={'class': 'form-control'},choices=((False, 'No'), (True, 'Si'))),
			'plazas': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'default':0}),
			'plazas_dto': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'default':0}),
			'plazas_dto_ocupadas': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'default':0}),
            'otracuenta': forms.Select(attrs={'class': 'form-control'},choices=((False, 'No'), (True, 'Si'))),
			'cuenta': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
				'placeholder': 'Cuenta...'
			}),
            'activo': forms.Select(attrs={'class': 'form-control', 'default':False},choices=((False, 'No Activo'), (True, 'Activo'))),
			'user': forms.NumberInput(attrs={'class': 'form-control input-lg mb-2'}),
        }
        labels = {
            'denominacion':'', 'lugar':'', 'descripcion': '', 'imagen':'Imágen', 
            'inicio':'Inicio', 'programa':'Programa', 'otracuenta':'Otra Cuenta', 'cuenta':'Cuenta'
        }


class MateriaUpdateForm(forms.ModelForm):

    class Meta:
        model = Materia
        fields = ('denominacion', 'activo', 'lugar','finicio', 'ffin', 'hinicio','hfin', 'descuento', 
				'descripcion', 'programa', 'imagen', 'dirigido', 'plazas', 'horas','creditos', 
				'importe', 'aplica_dto', 'plazas_dto', 'otracuenta','cuenta','observaciones', 'user')

        widgets = {
			'user': forms.NumberInput(attrs={'class': 'form-control input-lg mb-2', 'hidden': True}),
			'denominacion': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
                'placeholder': 'Denominación...', 'required': True
			}),
			'lugar': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
				'placeholder': 'Lugar de Celebración...', 'required': True
			}),
			'descripcion': forms.Textarea(attrs={'class': 'form-control input-lg mb-2',
                'required': True
			}),
			'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-2'}),			
			'finicio': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'date',}),
			'hinicio': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'time',}),
			'ffin': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'date',}),
			'hfin': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'time',}),
			'programa': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-2'}),
			'dirigido': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
				'placeholder': 'Dirigido a...'
			}),
			'descuento': forms.SelectMultiple(attrs={'class': 'form-control mb-2'}),
			'creditos': forms.NumberInput(attrs={'class': 'form-control mb-2', 'step':0.25, 'min':0, 'default':0}),
			'horas': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'default':0}),
			'importe': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'max':100.00, 'default':0}),
			'plazas': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'default':0}),
            'aplica_dto': forms.Select(attrs={'class': 'form-control'},choices=((False, 'No'), (True, 'Si'))),
			'plazas': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'default':0}),
			'plazas_dto': forms.NumberInput(attrs={'class': 'form-control mb-2', 'min':0, 'default':0}),
            'otracuenta': forms.Select(attrs={'class': 'form-control'},choices=((False, 'No'), (True, 'Si'))),
			'cuenta': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
				'placeholder': 'Cuenta...'
			}),
            'activo': forms.Select(attrs={'class': 'form-control', 'default':False},choices=((False, 'No Activo'), (True, 'Activo'))),
        }
        labels = {
            'denominacion':'', 'lugar':'', 'descripcion': '', 'imagen':'Imágen', 
            'inicio':'Inicio', 'programa':'Programa', 'otracuenta':'Otra Cuenta', 'cuenta':'Cuenta'
        }


class MateriaPonentesUpdateForm(BSModalForm):

    class Meta:
        model = Materia
        fields = ('ponente', )

        widgets = {
            'ponente': forms.SelectMultiple(attrs={'class': 'form-control mb-2'}),
        }
        labels = {
            'ponente':'Ponentes Disponibles',
        }

class MateriaApuntesForm(BSModalForm):
    class Meta:
        model = Apunte
        fields = ('des_apunte', 'fichero', )

        widgets = {
			'des_apunte': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
				'placeholder': 'Descripción del fichero ...', 'required':True
			}),
			'fichero': forms.FileInput(attrs={'class': 'form-control-file mb-2', 'required':True}),
        }

class MateriaPonenciaForm(BSModalForm):
    class Meta:
        model = Ponencia
        fields = ('denominacion', 'fecha', 'hinicio', 'hfin', 'ponente', )

        widgets = {
			'denominacion': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
				'placeholder': 'Descripción de la Ponencia ...', 'required':True
			}),
			'fecha': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'date',}),
			'hinicio': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'time',}),
			'hfin': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'time',}),
            'ponente': forms.SelectMultiple(attrs={'class': 'form-control mb-2'}),
        }
 