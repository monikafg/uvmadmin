from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['title', 'subject', 'content', 'image', 'published', 'author', 'galeria', 'fichero']
        widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control input-lg mt-2 mb-2',
                'placeholder': 'Título...', 'required': True
			}),
			'subject': forms.TextInput(attrs={'class': 'form-control input-lg mb-2',
				'placeholder': 'Entradilla...', 'required': True
			}),
			'content': forms.Textarea(attrs={'class': 'form-control input-lg mb-2',
                'required': True
			}),
			'image': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-2'}),
			'published': forms.DateTimeInput(attrs={'class': 'form-control input-lg mb-2'}),
			'author': forms.NumberInput(attrs={'class': 'form-control input-lg mb-2'}),
		    'galeria': forms.Select(attrs={'class': 'form-control mb-2'}),
			'fichero': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-2'}),
        }
        labels = {
            'title':'', 'subject':'', 'content': '', 'image':'', 
            'published':'Fecha de Publicación', 'galeria':'Galería de Fotos'
        }

