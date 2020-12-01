from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Historia(models.Model):
    autor = models.ForeignKey(User, on_delete=CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    imagen = models.ImageField(upload_to='imagenes/', blank=True)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    


    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "historia"
        verbose_name = "historia"
        verbose_name_plural = "historias"
        ordering = ["id"]
