# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-06 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planoDeManutencao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemDeServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, unique=True)),
                ('tipo_da_requisicao', models.CharField(choices=[('CO', 'CORRETIVA'), ('PR', 'PREVENTIVA')], max_length=40)),
                ('divisao', models.CharField(default='none', max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='none', max_length=40)),
                ('unidadeRequisitante', models.CharField(default='none', max_length=80)),
                ('description_full', models.TextField()),
                ('description_brief', models.TextField(max_length=140)),
                ('planosDeMan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planoDeManutencao.PlanoDeManutencao')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
