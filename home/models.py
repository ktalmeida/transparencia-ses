from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class PaginaInicial(Page):
    conteudo = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('conteudo', classname="full"),
    ]
