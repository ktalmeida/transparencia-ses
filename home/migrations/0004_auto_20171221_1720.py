# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='PaginaInicial',
        ),
        migrations.RenameField(
            model_name='paginainicial',
            old_name='body',
            new_name='conteudo',
        ),
    ]
