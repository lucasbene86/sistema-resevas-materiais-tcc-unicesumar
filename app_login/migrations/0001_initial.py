# Generated by Django 4.0.3 on 2022-05-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TentativaLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_usuario', models.CharField(max_length=20, verbose_name='IP_Usuario')),
                ('horario', models.CharField(max_length=10, verbose_name='Horario')),
                ('tentativas', models.CharField(max_length=1, verbose_name='Tentantiva')),
            ],
        ),
    ]
