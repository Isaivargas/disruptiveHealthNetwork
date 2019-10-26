from django.db import models

# Create your models here.
class Pregunta(models.Model):
    descripcion = models.CharField(max_length=200)
    texto = models.CharField(max_length=200)

