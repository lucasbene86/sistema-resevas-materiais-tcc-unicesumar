from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role, remove_role, get_user_roles, RolesManager
from rolepermissions.decorators import has_permission_decorator, has_role_decorator

from app_admin.pack.verificar_nivel_usuario import nivel_usuario
from dotenv import load_dotenv
import os

load_dotenv()

#@login_required(login_url='/login')
@has_permission_decorator('cadastrar_funcionarios')  # Apenas usuario com acesso
def admin_contas(request):

    # Captura ip do arquivo .env
    host_name_server = os.getenv('IP_SERVER')

    botao_apagar = request.GET.get('excluir', '')  # Request do botão apagar usuario.
    botao_alterar = request.GET.get('alterar', '')  # Request do botão alterar.


    # Obter usuarios da tabela auth_user
    id = []
    login = []
    nome = []
    data_cadastro = []
    nivel_acesso = []
    status = []
    dado_banco_dados = User.objects.all()
    lista_valores_banco = list(dado_banco_dados.values())
    for i in range(len(lista_valores_banco)):
        id.append(lista_valores_banco[i].get("id"))
        login.append(lista_valores_banco[i].get("username"))
        nome.append(lista_valores_banco[i].get("first_name"))
        data_cadastro.append(lista_valores_banco[i].get("date_joined"))
        status.append(lista_valores_banco[i].get("is_active"))

        # Grupo de cada usuario.
        user = User.objects.get(username = str((lista_valores_banco[i].get("username"))))
        # perm_names = set(p for role in roles for p in role.permission_names_list()
        grupos = user.groups.filter(name__in=RolesManager.get_roles_names())
        if str(grupos.get()) == 'funcionario': #
            nivel_acesso.append('Func.')
        elif str(grupos.get()) == 'coordenador':
            nivel_acesso.append('Coord.')
        elif str(grupos.get()) == 'administrador':
            nivel_acesso.append('Admin')


    # Organiza o codigo HTML para Tabela de usuarios
    codigo_tabela = ''
    for i in range(len(id)):
        if str(nivel_acesso[i]) == 'Admin':
            pass
        else:
            # Formatar a data
            data = str(data_cadastro[i]).split(' ')
            data.pop()
            data = ''.join(data)
            data = data.split('-')
            data_formatada = data[2] + '/' + data[1] + '/' + data[0]

            img = ''
            if str(status[i]) == 'True':
                img = '''<img src="/static/images/icone_ativo_sim.png" alt="on">'''
            else:
                img = '''<img src="/static/images/icone_ativo_nao.png" alt="off">'''


            codigo_tabela = codigo_tabela + f'''<tr>
                                                    <td class="coluna_id">{id[i]}</td>
                                                    <td>{nome[i]}</td>
                                                    <td>{login[i]}</td>
                                                    <td class='coluna_data'>{data_formatada}</td>
                                                    <td>{nivel_acesso[i]}</td>
                                                    <td class="imagem_status">{img}</td>
                                                </tr>'''


    exibir_front_end = {
        'dados_tabela':codigo_tabela,
        'host_name_server':host_name_server
    }


    # Apaga o usuario do banco de dados.
    if botao_apagar == 'excluir':
        id_item = request.GET.get('id_exclusao', '')
        user = User.objects.get(id=id_item)
        user.delete()

        print(id_item)
        return redirect('admin_contas')

    # Altera o usuario no banco de dados.
    if botao_alterar == 'alterar':
        id_usuario = request.GET.get('id_selecao', '')
        novo_nome = request.GET.get('novo_nome', '')
        novo_usuario = request.GET.get('novo_login', '')
        dado_nivel_acesso = request.GET['nivel_funcionario']
        status_usuario = request.GET.get('status_usuario', '')

        user = User.objects.get(id=id_usuario)


        # Altera o nome do usuario
        def altera_nome_usuario(usuario):
            user.first_name = usuario
            user.save()


        # Altera o status do usuario de ativo/inativo
        def altera_status_usuario(status):
            user.is_active = status
            user.save()
        
        # Troca de grupo para nivel de acesso o usuario 
        if str(dado_nivel_acesso) == 'funcionario':
            assign_role(user, 'funcionario')
            remove_role(user, 'coordenador')
            print(dado_nivel_acesso)
        elif str(dado_nivel_acesso) == 'coordenador':
            assign_role(user, 'coordenador')
            remove_role(user, 'funcionario')
            print(dado_nivel_acesso)


        try:
            if str(novo_usuario) == str(user):
                altera_nome_usuario(novo_nome)
                if status_usuario == 'on':
                    altera_status_usuario(True)
                else:
                    altera_status_usuario(False)
            else:
                # Verifica se já existe usuario cadastrado
                if User.objects.filter(username=novo_usuario).exists():
                    msg = """<script type="text/javascript">alert("Atenção! Usuário já existente!");
                            window.history.pushState("object or string", "Title", "/admin_contas/")</script>
                        """
                    popup = {
                        'dados_tabela':codigo_tabela,
                        'popup':msg,
                    }
                    return render(request, 'admin_contas.html', popup)
                else:
                    user.username = novo_usuario
                    user.save()
                    return redirect('admin_contas')

        except:
            print('dados errados')
        return redirect('admin_contas')

    # Adicionar funcionario
    if request.method == "POST":
        dado_nome = request.POST['nome']  # Puxa os dados do input HTML #
        dado_login = request.POST['login']  # Puxa os dados do input HTML #
        dado_senha0 = request.POST['senha']
        dado_senha = request.POST['senha1']  # Puxa os dados do input HTML #
        dado_nivel_acesso = request.POST['nivel_funcionario']
        dado_status = request.POST['status_funcionario']


        if len(dado_senha) >= 8 and dado_senha0 == dado_senha:
            print('Senha maior do que 8 caracteres!')
            if dado_status == 'on':
                dado_status = True
            else:
                dado_status = False

            # Adiciona o usuario para autenticação #
            try:
                user = User.objects.create_user(username=dado_login, first_name=dado_nome, password=dado_senha)
                user.is_staff = False
                user.is_active = dado_status
                user.save()

                if nivel_usuario(dado_nivel_acesso) == '1':
                    assign_role(user, 'funcionario') # Grupo do usuario

                elif nivel_usuario(dado_nivel_acesso) == '2':
                    #assign_role(user, 'administrador') # Usuario admin
                    assign_role(user, 'coordenador') # Grupo do usuario

                return redirect('admin_contas')
            except:
                msg = """<script type="text/javascript">alert("Atenção! Usuário já existente!");
                            window.history.pushState("object or string", "Title", "/admin_contas/")</script>
                        """
                user_existente={
                    'dados_tabela':codigo_tabela,
                    'popup':msg,
                    }
                return render(request, 'admin_contas.html', user_existente)
        else:
            print('senha pequena')
            msg = """<script type="text/javascript">alert("Atenção! Senha pequena ou diferentes.");
                            window.history.pushState("object or string", "Title", "/admin_contas/")</script>
                        """
            senha_errada = {
                'dados_tabela':codigo_tabela,
                'popup':msg,
                }
            return render(request, 'admin_contas.html', senha_errada)

    return render(request, 'admin_contas.html', exibir_front_end)
