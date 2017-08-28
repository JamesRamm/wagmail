# -*- coding: utf-8 -*-
"""
Database models for wagmail.
"""
from __future__ import absolute_import, unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.template import Template, Context
from django.core.mail import send_mail

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


class EmailTemplate(models.Model):
    '''Rich text (HTML) email templates which allow value substitutions using the
    django template language.
    '''
    subject = models.CharField(max_length=64, help_text="The subject of emails sent using this template")
    description = models.CharField(max_length=255, help_text="Short description of the email template. Not included in sent emails")
    body = RichTextField(help_text="Main body of the email. When connecting to model signals, the model instance is available as the `instance` context value")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    panels = [
        FieldPanel('subject', classname='full'),
        FieldPanel('description', classname='full'),
        FieldPanel('body', classname='full'),
    ]

    def send(self, recipients, **kwargs):
        '''Render and send the email
        '''
        template = Template(self.body)
        kwargs['recipients'] = recipients
        context = Context(kwargs)
        message = template.render(context)

        send_mail(
            self.subject,
            message,
            'from@example.com',
            recipients,
            fail_silently=False,
        )
