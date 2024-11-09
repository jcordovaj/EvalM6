from django.db import models

# Create your models here.

class Cotizacion(models.Model):
    nombre   = models.CharField(max_length=100)
    email    = models.EmailField()
    mensaje  = models.CharField(max_length=200)


