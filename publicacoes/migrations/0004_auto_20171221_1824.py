# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 18:24
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0003_auto_20171221_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paginapublicacao',
            name='conteudo',
            field=wagtail.wagtailcore.fields.StreamField((('conteudo', wagtail.wagtailcore.blocks.RichTextBlock(null=True)), ('tabela', wagtail.contrib.table_block.blocks.TableBlock()))),
        ),
    ]