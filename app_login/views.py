from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, password_validation
from app_login.pack.inserir_verificacao import inserir_verificacao_login

import os
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from dotenv import load_dotenv

load_dotenv()

# IP do usuario.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Create your views here.
def login_user(request):
    # Caso seja o primeiro acesso do usuario, é criado um usuario padrão com acesso 'admin' senha '12345678'.
    primeiro_acesso = os.getenv('ACESSO')

    if primeiro_acesso == 'True':
        user = User.objects.create_user(username='admin', first_name='Temporário', password='12345678')
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        assign_role(user, 'administrador') # Usuario admin temporário
        print('user')
    else:
        pass


    # faz o logout do user
    logout(request)

    ip_user = (get_client_ip(request))
    status_login = inserir_verificacao_login(ip_user)
    status = 'ATENÇÃO! Acesso temporariamente bloqueado.'

    if status_login == 'True':
        tentativa_login = {
            'login': status,
            'nao_visivel': 'style=display:flex;'
        }
        return render(request, 'login.html', tentativa_login)

    if request.method == "POST":
        user = request.POST['usuario']  # Puxa os dados do input HTML #
        senha = request.POST['senha']  # Puxa os dados do input HTML #

        usuario = authenticate(request, username=user, password=senha)
        if usuario is not None:
            print('Logado')
            login(request, usuario)  # Loga no user do django
            return redirect('index')
        else:
            print('usuario incorreto!')

    tentativa_login = {
        'login':status,
        'nao_visivel':'style=display:none;'
    }
    return render(request, 'login.html', tentativa_login)
