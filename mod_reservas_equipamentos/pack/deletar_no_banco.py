# Modulo para deletar no banco de dados os dados tratados.
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from mod_reservas_equipamentos.models import DadosReserva

def deletar_item(id_item):
    # inserir dados no banco de dados
    obj = get_object_or_404(DadosReserva, id = int(id_item))

    # deletar objeto
    obj.delete()
    # return HttpResponseRedirect("/")