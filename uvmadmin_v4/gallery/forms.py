from django import forms
from PIL import Image
from .models import Album


class ImageFileInput(forms.ClearableFileInput):

    def validate(self, value):
        return super.validate(value)


class ImageCreateForm(forms.Form):
    data = forms.FileField(widget=ImageFileInput(attrs={'multiple': True}))

    def clean(self):
        """ Validate files by checking they can be opened by PIL """
        # cleaned_data = super(ImageCreateForm, self).clean()
        image_files = self.files.getlist('data')
        invalid_images = []
        for img in image_files:
            try:
                i = Image.open(img)
                i.verify()
            except (IOError, SyntaxError):
                invalid_images += [img]
        if invalid_images:
            image_names = [i._name for i in invalid_images]
            raise forms.ValidationError("Unable to add invalid images: {0}".format(image_names))


#=======================================================
# AlbumCreateForm: Formulario para crear un nuevo álbum
#=======================================================
class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ['title', 'images']   

        widgets = {
			'title': forms.TextInput(attrs={
				'placeholder': 'Título galería...',
				'class': 'form-control input-lg mt-2 mb-2',
                'required': True
			}),
			'images': forms.SelectMultiple(attrs={
				'class': 'form-control input-lg mb-2',
			})
		}
        labels = {
            'title':''
        }
		

