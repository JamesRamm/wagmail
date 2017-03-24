# -*- coding: utf-8 -*-
"""
Database models for wagmail.
"""

from __future__ import absolute_import, unicode_literals
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


class EmailTemplate(Page):
    parent_page_types = ['wagtailcore.Page']
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    body = StreamField([
        ('template', blocks.RawHTMLBlock()),
    ])

    content_panels = [
        FieldPanel('name', classname="full"),
        FieldPanel('description', classname="full"),
        StreamFieldPanel('body'),
    ]