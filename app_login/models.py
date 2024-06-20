from django.db import models

class TentativaLogin(models.Model):
    ip_usuario = models.CharField('IP_Usuario', max_length=20)
    horario = models.CharField('Horario', max_length=10)
    tentativas = models.CharField('Tentantiva', max_length=1)
