

from django.db import models

# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=80)
    local = models.TextField()
    dia = models.DateField()
    hora = models.TimeField()
    numero_participantes = models.IntegerField()


class Pessoa(models.Model):
    nome = models.TextField()
    data_nascimento = models.DateField()
    eventos = models.ManyToManyField(Evento)

















