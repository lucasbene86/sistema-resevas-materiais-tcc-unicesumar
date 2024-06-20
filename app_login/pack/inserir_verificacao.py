# Modulo para salvar no banco de dados os dados tratados.
from datetime import datetime, time
from re import T

from app_login.models import TentativaLogin


def inserir_verificacao_login(ip_user):
    data_hora_atual = datetime.now() # data e hora atual
    hora_atual = data_hora_atual.strftime('%H:%M') # Hora atual do sistema
    dado_banco_dados = TentativaLogin.objects.all()
    lista_valores_banco = list(dado_banco_dados.values())

    ip_lista = []
    for i in range(len(lista_valores_banco)):
        ip_lista.append(lista_valores_banco[i].get('ip_usuario'))

    linha_ip = ''
    verificar_horario = ''
    verificar_tentativa = ''
    if ip_lista.count(ip_user) == 1:
        for i in range(len(lista_valores_banco)):
            ip = lista_valores_banco[i].get('ip_usuario')
            if ip == ip_user:
                linha_ip = lista_valores_banco[i]
                id_linha = linha_ip.get('id')
                verificar_horario = list(linha_ip.get('horario'))
                hora_atual_lista = list(hora_atual)
                verificar_horario.pop(2)
                hora_atual_lista.pop(2)

                hora_login = ''.join(verificar_horario)
                hora_atual = ''.join(hora_atual_lista)
                diferenca_minutos = int(hora_atual) - int(hora_login)
                 #print(diferenca_minutos)

                # Verificar se foi solicitado login o IP solicitou nos 5 minutos.
                if diferenca_minutos >= 0 and diferenca_minutos <= 5:
                    verificar_tentativa = int(linha_ip.get('tentativas'))
                    if int(verificar_tentativa) < 5:
                        # Alterar numero de tentativa no banco de dados.
                        TentativaLogin.objects.filter(id=id_linha).update(
                            tentativas = int(verificar_tentativa) + 1,
                        )
                    else:
                        tentativa_suspeita_login = 'True'
                        return tentativa_suspeita_login
                else:
                    # Deletar linha na tabela do banco.
                    # TentativaLogin.objects.filter(id=int(id_linha)).delete()
                    linha = TentativaLogin.objects.get(id=int(id_linha))
                    linha.delete()

    else:
        # inserir dados no banco de dados
        tentiativa_login = TentativaLogin(
            ip_usuario = ip_user,
            horario = hora_atual,
            tentativas = '0',
        )
        tentiativa_login.save()
        tentativa_suspeita_login = 'False'
        return tentativa_suspeita_login
