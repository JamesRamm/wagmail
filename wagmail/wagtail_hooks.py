from django.core.urlresolvers import reverse

from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.menu import MenuItem

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from wagmail.models import EmailTemplate


# class WagmailModelAdmin(ModelAdmin):
#     model = EmailTemplate
#     menu_order = 900
#     menu_icon = 'mail'
#     menu_label = 'Mail'
#     add_to_settings_menu = False
#     exclude_from_explorer = True
#     list_display = ('name', 'description')
#     list_filter = ('name',)

# modeladmin_register(WagmailModelAdmin)


@hooks.register('register_admin_menu_item')
def register_wagmail():
  return MenuItem('Mail', reverse('wagmail'), classnames='icon icon-mail', order=900)  