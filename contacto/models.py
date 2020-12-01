from django.db import models
from django.utils import timezone

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=150)
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "contacto"
        verbose_name = "contacto"
        verbose_name_plural = "contactos"
        ordering = ["id"]
    