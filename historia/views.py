from django.shortcuts import render
from django.views.generic import * 
from historia.models import Historia

# Create your views here.

class Listahistoria(ListView):
    model = Historia
    template_name = "historias/historia.html"


class DetalleHis(DetailView):
    model = Historia
    template_name = "historias/detallehis.html"