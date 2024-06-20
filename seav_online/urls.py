"""seav_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_sistema_web_seav/', admin.site.urls),
    path('', include('mod_reservas_equipamentos.urls')), # App de reserva de equipamentos
    path('login/', include('app_login.urls')), # App de login (rotas)
    path('admin_contas/', include('app_admin.urls')), # App de admin contas (rotas)
    path('alterar_senha/', include('app_alterar_senha.urls')), # App para alterar senha (rota)
]
