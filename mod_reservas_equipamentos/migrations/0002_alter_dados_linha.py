# Generated by Django 4.0.3 on 2022-03-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mod_reservas_equipamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='linha',
            field=models.CharField(max_length=500, verbose_name='CPF'),
        ),
    ]
