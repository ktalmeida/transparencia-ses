import os
from transparencia.settings.base import BASE_DIR

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import \
    FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from django.db import models
from wagtail.wagtailsearch import index
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks

TABLE_PATH = os.path.join(BASE_DIR, 'publicacoes/templates/table.html')


class PaginaInicialPublicacoes(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    subpage_types = [
        'publicacoes.PaginaPublicacao',
        'publicacoes.PaginaInicialPublicacoes']


class TableBlock(blocks.StreamBlock):
    conteudo = blocks.RichTextBlock(null=True)
    tabela = TableBlock(template=TABLE_PATH, table_options={
        'startCols': 5,
        'autoWrapRow': True,
        'autoWrapCol': True,
        'minSpareRows': 1,
        'colHeaders': (
            'Item', 'Código SIGMA', 'Quantidade',
            'Valor unitário R$', 'Unidade de medida'),
        'editor': 'handsontable',
        'rowHeaders': False
    })


class PaginaPublicacao(Page):
    conteudo = StreamField(TableBlock())
    date = models.DateField("Data de publicação")

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('conteudo'),
        index.FilterField('date'),
    ]

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('conteudo', classname="full")
    ]

    parent_page_types = ['publicacoes.PaginaInicialPublicacoes']
