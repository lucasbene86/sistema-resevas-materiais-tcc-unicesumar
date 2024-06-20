from django.urls import path
from .views import admin_contas

urlpatterns = [
    path('', admin_contas, name='admin_contas'),
]