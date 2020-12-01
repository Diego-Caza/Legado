from django.urls.base import reverse
from contacto.forms import ContactoForm
from contacto.models import Contacto
from django.shortcuts import render
from django.views.generic import CreateView
from contacto.models import Contacto
from .forms import ContactoForm
from django.urls import reverse_lazy

# Create your views here.

class CrearContacto(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = "contacto/crearcontacto.html"

    def get_success_url(self):
        return reverse('home')
    