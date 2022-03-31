from django import forms
from django.db import models


class Pet(models.Model):
    PORTE = (
    ('MICRO','Micro'),
    ('PEQUENO','Pequeno'),
    ('MEDIO','Médio'),
    ('GRANDE','Grande'),
    ('GIGANTE','Gigante'),
    )
    CHOICES = (('M','Macho'),('F','Fêmea'))

    nome = models.CharField(max_length=100)
    nasc = models.DateField(blank=True)
    especie = models.CharField(max_length=20)
    raca= models.CharField(max_length=15,blank=True)
    cor = models.CharField(max_length=100,blank=True)
    idade = models.IntegerField(blank=True)
    porte = models.TextField(choices=PORTE,max_length=15,default=0)
    sexo = models.CharField(choices=CHOICES,max_length=10, default=0)
    # date_cricao = models.DateField()