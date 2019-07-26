# Generated by Django 2.2.3 on 2019-07-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=255, verbose_name='Celular')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=255, verbose_name='Gênero')),
                ('ativo', models.BooleanField(default=True)),
                ('data_de_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
