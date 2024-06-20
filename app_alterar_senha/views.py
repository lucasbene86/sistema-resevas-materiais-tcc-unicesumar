from email import message
from math import radians
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dotenv import load_dotenv
import os

load_dotenv()

@login_required(login_url='/login')
def alterar_senha(request):
    # Captura ip do arquivo .env
    host_name_server = os.getenv('IP_SERVER')

    if request.method == 'POST':
        dado_senha_atual = request.POST['senha_atual']
        dado_nova_senha = request.POST['senha']
        dado_senha_repetida = request.POST['senha1']

        # ALterar senha do user logado
        username = request.user

        try:
            user = User.objects.get(username=username)
            if user.check_password(dado_senha_atual):
                user.set_password(dado_senha_repetida)
                user.save()
                print('ok')
                # logout(request)
                messages.success(request, 'A senha foi alterada com sucesso!')
                # return redirect('alterar_senha')
            else:
                messages.error(request, 'A senha digitada está incorreta!')
                return redirect('alterar_senha')
        except:
            print('dados errados')
    
    ip_server = {
        'host_name_server':host_name_server
    }

    return render(request, 'alterar_senha.html', ip_server)