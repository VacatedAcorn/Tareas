from django.db import models

# Create your models here.

class pizzeria(models.Model):
    sabor= models.CharField(max_length=20, blank=True, null=True)
    tipo= models.CharField(max_length=20, blank=True, null=True)
    tamanio= models.CharField(max_length=20, blank=True, null=True)