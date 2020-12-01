from django.urls import path
from contacto.views import CrearContacto

urlpatterns = [
    
    path('', CrearContacto.as_view(), name='newcomentario'),
    

]