from posixpath import split
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import DadosReserva
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from urlparams.redirect import param_redirect

from datetime import date, datetime, time
from mod_reservas_equipamentos.pack.meses import mes
from mod_reservas_equipamentos.pack.inserir_no_banco import banco_de_dados
from mod_reservas_equipamentos.pack.modificar_no_banco import modificar_banco_de_dados
from mod_reservas_equipamentos.pack.deletar_no_banco import deletar_item
from dotenv import load_dotenv
import os

load_dotenv()

@login_required(login_url='/login')
def index(request):
    # Adiciona o usuario para autenticação #
    '''user = User.objects.create_user('admin', '', 'admin')
    user.is_staff = True
    user.save()'''

    # Captura ip do arquivo .env
    host_name_server = os.getenv('IP_SERVER')

    nome_user_logado = str(request.user.get_short_name())

    # Função para formatar o codigo e quantidade de equipamentos.
    def formato_equipamento(numero, tipo_equipamento):
        equipamento_str = str(tipo_equipamento[numero])
        equipamento_lista = list
        codigo_html = ''
        equipamento_lista = equipamento_str.split(' ')
        # print(equipamento_lista)
        # print(equipamento_lista.count('note'))

        total_note = equipamento_lista.count('note')
        total_som = equipamento_lista.count('som')
        total_projetor = equipamento_lista.count('projetor')
        total_outros = equipamento_lista.count('outros')

        if total_note > 0:
            codigo_html = f'<img src="../static/images/icone_notebook.png" alt="Note"><label id="contem_note" class="quatidade_equi">{total_note}</label>'
        if total_som > 0:
            codigo_html = codigo_html + f'<img src="../static/images/icone_som.png" alt="Som"><label id="contem_som" class="quatidade_equi">{total_som}</label>'
        if total_projetor > 0:
            codigo_html = codigo_html + f'<img src="../static/images/icone_datashow.png" alt="Proje"><label id="contem_projetor" class="quatidade_equi">{total_projetor}</label>'
        if total_outros > 0:
            codigo_html = codigo_html + f'<img src="../static/images/icone_outros.png" alt="Outros"><label id="contem_outros" class="quatidade_equi">{total_outros}</label>'

        # print(codigo_html)
        return codigo_html


    def formato_hora(numero, tipo_hora):
        hora_str = tipo_hora[numero]
        # print(hora_str)
        return hora_str


    def formato_status(numero, tipo_status):
        status_str = str(tipo_status[numero])
        codigo_html = str

        if status_str == 'sala':
            codigo_html = '<img id="emsala" src="../static/images/icone_em_sala.png" alt="Em sala">'
        elif status_str == 'retirado':
            codigo_html = '<img id="retirado" src="../static/images/icone_retirado.png" alt="Retirado">'
        else:
            codigo_html = '<img id="reserva" src="../static/images/icone_agendado.png" alt="Reserva">'

        return codigo_html


    botao_pagina = request.GET.get('Next', '')  # Request do Botão que foi clicado.
    botao_adicionar = request.GET.get('adicionar')   # Request do botão adicionar.
    botao_alterar = request.GET.get('alterar')  # Request do botão alterar.
    botao_excluir = request.GET.get('excluir')  # Request do botão excluir.
    botao_estatistica = request.GET.get('estatistica')

    # Data atual para iniciar o sistema
    data_hora_atual = datetime.now() # data e hora atual
    data_atual = str(data_hora_atual.strftime('%Y-%m-%d'))  # Data atual do sistema
    # hora_atual = data_hora_atual.strftime('%H:%M') # Hora atual do sistema

    data_selecionada = []
    data_selecionada = data_atual.split('-')

    # Mês
    mes_atual = str(mes(data_selecionada[1]))
    data_selecionada.append(mes_atual)

    # identificar qual a data selecionada (metodo GET)
    if request.method == "POST":
        data_selecao = request.POST['bday']  # Puxa os dados do input HTML #
        data_selecionada.clear()
        data_lista = []

        data_lista = data_selecao.split('-')
        data_selecionada.append(data_lista[0])
        data_selecionada.append(data_lista[1])
        data_selecionada.append(data_lista[2])

        # Mês Selecionado
        mes_atual = str(mes(data_selecionada[1]))
        data_selecionada.append(mes_atual)

        data_atual = data_selecao

    # ler dados do banco de dados
    dado_banco_dados = DadosReserva.objects.all()
    lista_valores_banco = list(dado_banco_dados.values())
    lista_valores_banco_dia = []
    for i in range(len(lista_valores_banco)):
        dicionario = {}
        dicionario = lista_valores_banco[i]
        if dicionario.get('data_reserva') == data_atual:
            lista_valores_banco_dia.append(dicionario)

    #print(lista_valores_banco_dia)
    dados_separados_id = []
    dados_separados_local = []
    dados_separados_data_reserva = []
    dados_separados_horario = []
    dados_separados_solicitante = []
    dados_separados_departamento = []
    dados_separados_equipamento = []
    dados_separados_status = []
    dados_separados_observacoes = []

    for i in range(len(lista_valores_banco_dia)):
        dados_separados_id.append(lista_valores_banco_dia[i].get('id'))
        dados_separados_local.append(lista_valores_banco_dia[i].get('local'))
        dados_separados_data_reserva.append(lista_valores_banco_dia[i].get('data_reserva'))
        dados_separados_horario.append(lista_valores_banco_dia[i].get('horario'))
        dados_separados_solicitante.append(lista_valores_banco_dia[i].get('solicitante'))
        dados_separados_departamento.append(lista_valores_banco_dia[i].get('departamento'))
        dados_separados_equipamento.append(lista_valores_banco_dia[i].get('equipamento'))
        dados_separados_status.append(lista_valores_banco_dia[i].get('status'))
        dados_separados_observacoes.append(lista_valores_banco_dia[i].get('observacoes'))

    codigo_tabela = ''
    for i in range(len(dados_separados_id)):

        codigo_tabela = codigo_tabela + f"""<tr class="linhas_tabela">
                            <td class="coluna_id">{dados_separados_id[i]}</td>
                            <td>{dados_separados_local[i]}</td>
                            <td>{formato_hora(i, dados_separados_horario)}</td>
                            <td>{dados_separados_solicitante[i]}</td>
                            <td class="coluna_departamento">{dados_separados_departamento[i]}</td>
                            <td class="coluna_equipamento imagem_equipamento">
                                {formato_equipamento(i, dados_separados_equipamento)}
                            </td>
                            <td class="coluna_status">
                                {formato_status(i, dados_separados_status)}
                            </td>
                            <td>{dados_separados_observacoes[i]}</td>
                        </tr>"""



    # Redirecionar para cada pagina de acordo com o botão clicado.
    if botao_pagina == 'btn_reservas_equipamentos':
        return redirect('index')
    elif botao_pagina == 'btn_cadastro_funcionario':
        return redirect('admin_contas')


    # Dados do formulario para adicionar novo equipamento em sala.
    if botao_adicionar == 'adicionar':
        dado_data = request.GET.get('bday')
        dado_local = request.GET.get('local')
        dado_solicitante = request.GET.get('solicitante')
        dado_equipamento_notebook = int(request.GET.get('notebook'))
        dado_equipamento_som = int(request.GET.get('som'))
        dado_equipamento_projetor = int(request.GET.get('projetor'))
        dado_equipamento_outros = int(request.GET.get('outros'))
        dado_horario_inicio = request.GET.get('horario_inicio')
        dado_horario_fim = request.GET.get('horario_fim')
        dado_departamento = request.GET.get('departamento')
        dado_observacoes = request.GET.get('observacoes')
        dado_status = request.GET.get('status_equipamento')


        # identificar quantos notes, sons e projetores foram selecionados.
        dado_equipamento = ''
        for i in range(dado_equipamento_notebook):
            dado_equipamento = dado_equipamento + 'note '
        for i in range(dado_equipamento_som):
            dado_equipamento = dado_equipamento + 'som '
        for i in range(dado_equipamento_projetor):
            dado_equipamento = dado_equipamento + 'projetor '
        for i in range(dado_equipamento_outros):
            dado_equipamento = dado_equipamento + 'outros '
        # print(dado_equipamento)

        # horario de inicio e fim.
        dado_horario = str(dado_horario_inicio + ' - ' + dado_horario_fim)


        banco_de_dados(
            dado_data,
            dado_local,
            dado_horario,
            dado_solicitante,
            dado_departamento,
            dado_equipamento,
            dado_status,
            dado_observacoes,
        )
        data = {
            'data_atual':data_atual,
            'dia':data_selecionada[2],
            'mes':data_selecionada[3],
            'dados_tabela':codigo_tabela,
            'user_logado':nome_user_logado,
            'host_name_server':host_name_server
        }
        print(data_atual)

        return redirect('index')
        # return render(request, 'index.html', data)

    # BOTÃO ALTERAR
    if botao_alterar == 'alterar':
        dado_id = request.GET.get('id_selecao')
        dado_data = request.GET.get('bday')
        dado_local = request.GET.get('local')
        dado_solicitante = request.GET.get('solicitante')
        dado_equipamento_notebook = int(request.GET.get('notebook'))
        dado_equipamento_som = int(request.GET.get('som'))
        dado_equipamento_projetor = int(request.GET.get('projetor'))
        dado_equipamento_outros = int(request.GET.get('outros'))
        dado_horario_inicio = request.GET.get('horario_inicio')
        dado_horario_fim = request.GET.get('horario_fim')
        dado_departamento = request.GET.get('departamento')
        dado_observacoes = request.GET.get('observacoes')
        dado_status = request.GET.get('status_equipamento')


        # identificar quantos notes, sons e projetores foram selecionados.
        dado_equipamento = ''
        for i in range(dado_equipamento_notebook):
            dado_equipamento = dado_equipamento + 'note '
        for i in range(dado_equipamento_som):
            dado_equipamento = dado_equipamento + 'som '
        for i in range(dado_equipamento_projetor):
            dado_equipamento = dado_equipamento + 'projetor '
        for i in range(dado_equipamento_outros):
            dado_equipamento = dado_equipamento + 'outros '
        # print(dado_equipamento)

        # horario de inicio e fim.
        dado_horario = str(dado_horario_inicio + ' - ' + dado_horario_fim)


        modificar_banco_de_dados(
            dado_id,
            dado_data,
            dado_local,
            dado_horario,
            dado_solicitante,
            dado_departamento,
            dado_equipamento,
            dado_status,
            dado_observacoes,
        )

        return redirect('index')
    
    # print(request.user) # Obter usuario cadastrado.
    # print(request.user.get_short_name()) # Obter o primeiro nome do user cadastrado.
    # print(request.user.get_full_name()) # Obter o nome e sobrenome do usuario cadastrado.


    # BOTÃO EXCLUIR
    if botao_excluir == 'excluir':
        id_item = request.GET.get('id_exclusao')
        deletar_item(id_item)
        return redirect('index')
        # return param_redirect(request, 'index')

    data = {
        'data_atual':data_atual,
        'dia':data_selecionada[2],        
        'mes':data_selecionada[3],
        'dados_tabela':codigo_tabela,
        'user_logado':nome_user_logado,
        'host_name_server':host_name_server
    }
    # BOTÃO ESTATISTICAS DOS EQUIPAMENTOS
    if botao_estatistica == 'estatistica':
        #return redirect('estatistica')
        return render(request, 'estatistica.html', data)

    return render(request, 'index.html', data)


@login_required(login_url='/login')
def versoes(request):
    # Captura ip do arquivo .env
    host_name_server = os.getenv('IP_SERVER')

    ip_server = {
        'host_name_server':host_name_server
    }

    return render(request, 'versoes.html', ip_server)


@login_required(login_url='/login')
def reserva(request):
    # Captura ip do arquivo .env
    host_name_server = os.getenv('IP_SERVER')

    ip_server = {
        'host_name_server':host_name_server
    }

    return render(request, 'reserva.html', ip_server)