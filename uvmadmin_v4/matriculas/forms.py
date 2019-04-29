from django import forms
from .models import Matricula

class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        fields = ('alumno', 'materia', 'lugar', 'estado', 'freserva', 'fpago', 'impreso')

        widgets = {
            'alumno': forms.Select(attrs={'class': 'form-control mb-2'}),
            'materia': forms.Select(attrs={'class': 'form-control mb-2'}),
            'lugar': forms.Select(attrs={'class': 'form-control mb-2'}),
            'estado': forms.Select(attrs={'class': 'form-control mb-2'}),
			'freserva': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'date',}),
			'fpago': forms.TextInput(attrs={'class': 'form-control mb-2', 'type':'date',}),
            'impreso': forms.Select(attrs={'class': 'form-control', 'default':False},choices=((False, 'No'), (True, 'Si'))),
        }

 