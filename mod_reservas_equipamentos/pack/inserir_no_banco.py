# Modulo para salvar no banco de dados os dados tratados.

from mod_reservas_equipamentos.models import DadosReserva

def banco_de_dados(data, dado_local, dado_horario_inicio, dado_solicitante, dado_departamento, dado_equipamento_notebook, dado_status, dado_observacoes):
    # inserir dados no banco de dados
    tabela_reserva_equipamentos = DadosReserva(
        data_reserva=data,
        local=dado_local,
        horario=dado_horario_inicio,
        solicitante=dado_solicitante,
        departamento=dado_departamento,
        equipamento=dado_equipamento_notebook,
        status=dado_status,
        observacoes=dado_observacoes
    )
    tabela_reserva_equipamentos.save()