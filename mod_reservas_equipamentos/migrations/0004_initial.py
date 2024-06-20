# Generated by Django 4.0.3 on 2022-03-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mod_reservas_equipamentos', '0003_delete_dados'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=100, verbose_name='Local')),
                ('horario', models.CharField(max_length=10, verbose_name='Horario')),
                ('solicitante', models.CharField(max_length=100, verbose_name='Solicitante')),
                ('departamento', models.CharField(max_length=10, verbose_name='Depart')),
                ('equipamento', models.CharField(max_length=500, verbose_name='Equipamentos')),
                ('status', models.CharField(max_length=200, verbose_name='Status')),
                ('observacoes', models.CharField(max_length=500, verbose_name='Observações')),
            ],
        ),
    ]