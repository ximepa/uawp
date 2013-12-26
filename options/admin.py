# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import GreetingPageOption, PageOption, Cheat
from django.utils.translation import ugettext_lazy as _


class PageOptionAdmin(admin.ModelAdmin):
    raw_id_fields = ['greeting_page_pk']
    fieldsets = [
        (_(u'Настройки:'), {
            'fields': (
                'greeting_page',
                'greeting_page_pk',
                'news_per_page',
                'news_max_count',
            )
        }),
        ]
    list_display = ('id', 'greeting_page', 'greeting_page_pk', 'news_per_page', 'news_max_count',)


class GreetingPageOptionAdmin(admin.ModelAdmin):
    pass


class CheatAdmin(admin.ModelAdmin):
    fieldsets = [
        (_(u'Настройки:'), {
            'fields': (
                'enable_cheats',
                'cheating_registered_users',
                'cheating_characters',
            )
        }),
        ]
    list_display = ('cheating_registered_users', 'cheating_characters', 'enable_cheats',)


admin.site.register(Cheat, CheatAdmin)
admin.site.register(PageOption, PageOptionAdmin)
admin.site.register(GreetingPageOption, GreetingPageOptionAdmin)
