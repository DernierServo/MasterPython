#Forms remplaza al HTML de un Formulario nativo.

from django import forms
from django.core import validators

class Form_Article(forms.Form):

    title = forms.CharField(
        label = 'Titulo 2',
        max_length = 20,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Colocar el título',
                'class': 'titulo_form_article'
            }
        ),
        validators = [
            validators.MinLengthValidator(4, 'El títulos es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El título está mal formado', 'invalid_title')

        ]
    )

    content = forms.CharField(
        label = 'Contenido 2',
        widget = forms.Textarea(
            attrs = {
                'placeholder': 'Colocar el título',
                'class': 'contenido_form_article'
            }            
        ),
        validators = [
            validators.MaxLengthValidator(20, 'Te has pasado con mucho texto!')
        ]
    )

    public_options = [
        (1, 'Sí'),
        (2, 'No')
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )