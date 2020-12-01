import historia
from historia.views import DetalleHis, Listahistoria
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.list import ListView
from historia import views

urlpatterns = [
    
    path('', Listahistoria.as_view(), name='home'),
    path('historia/<int:pk>/', DetalleHis.as_view(), name='detalle'),

]