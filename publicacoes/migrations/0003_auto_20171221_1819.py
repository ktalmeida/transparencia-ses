# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 18:19
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0002_paginapublicacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paginapublicacao',
            name='body',
        ),
        migrations.AddField(
            model_name='paginapublicacao',
            name='conteudo',
            field=wagtail.wagtailcore.fields.StreamField((('texto', wagtail.wagtailcore.blocks.RichTextBlock(null=True)), ('tabela', wagtail.contrib.table_block.blocks.TableBlock())), default=None),
            preserve_default=False,
        ),
    ]
