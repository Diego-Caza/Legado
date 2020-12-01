from django import forms
from django.forms import widgets
from contacto.models import Contacto
from django import forms


class ContactoForm(forms.ModelForm):
    class Meta():
        model = Contacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        required = ['nombre', 'email', 'mensaje']
        labels = {
            'nombre': 'Nombre completo:',
            'email': 'Email:',
            'asunto': 'Asunto:',
            'mensaje': 'Mensaje:'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su Apellido y Nombre/s',
                    'id':'nombre'
                    }
                ),
            'email': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'example@email.com',
                    'id':'email'
                }
                ),
            'asunto': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el asunto de su mensaje',
                    'id':'asunto'
                    }
                ),
            'mensaje': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el mensaje',
                    'id':'mensaje'
                    }
                )
        }
    

