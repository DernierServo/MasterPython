#Forms remplaza al HTML de un Formulario nativo.

from django import forms

class Form_Article(forms.Form):

    title = forms.CharField(
        label = 'Titulo'
    )

    content = forms.CharField(
        label = 'Contenido',
        widget = forms.Textarea
    )