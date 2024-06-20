from django.urls import path
from .views import index, versoes, reserva

urlpatterns = [
    path('', index, name='index'),
    path('versoes/', versoes, name='versoes'),
]