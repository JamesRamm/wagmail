# -*- coding: utf-8 -*-
"""
Database models for wagmail.
"""
from __future__ import absolute_import, unicode_literals
from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel,
    StreamFieldPanel
)

class FormField(AbstractFormField):
    page = ParentalKey('ContactForm', related_name='form_fields')

class ContactForm(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thankyou_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thankyou_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


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