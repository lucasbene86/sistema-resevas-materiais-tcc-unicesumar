from django.db import models

class DadosReserva(models.Model):
    data_reserva = models.CharField('Data', max_length=11)
    local = models.CharField('Local', max_length=100)
    horario = models.CharField('Horario', max_length=15)
    solicitante = models.CharField('Solicitante', max_length=100)
    departamento = models.CharField('Depart', max_length=10)
    equipamento = models.CharField('Equipamentos', max_length=500)
    status = models.CharField('Status', max_length=200)
    observacoes = models.CharField('Observações', max_length=500)