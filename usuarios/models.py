# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Usuarios(models.Model):
    nombre =models.CharField(max_length=50)
    apellidoP=models.CharField(max_length=50)
    apellidoM=models.CharField(max_length=50)
    correo = models.EmailField(max_length=256)
    usuario = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('created',)