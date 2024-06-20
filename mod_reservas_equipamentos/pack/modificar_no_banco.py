# Modulo para modificar no banco de dados os dados.

from mod_reservas_equipamentos.models import DadosReserva

def modificar_banco_de_dados(id_linha, data, dado_local, dado_horario, dado_solicitante, dado_departamento, dado_equipamento, dado_status, dado_observacoes):
    # inserir dados no banco de dados
    DadosReserva.objects.filter(id=id_linha).update(
        data_reserva = data,
        local = dado_local,
        horario = dado_horario,
        solicitante = dado_solicitante,
        departamento = dado_departamento,
        equipamento = dado_equipamento,
        status = dado_status,
        observacoes = dado_observacoes
    )
