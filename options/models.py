# -*- coding: utf-8 -*-
from django.db import models
from web.models import StaticPages
from django.utils.translation import gettext as _



class PageOption(models.Model):
    greeting_page = models.ForeignKey('GreetingPageOption', help_text=_(u'Показывать страницу приветствия или новостей'))
    greeting_page_pk = models.ForeignKey(StaticPages, help_text=_(u'id страницы приветствия'), blank=True, null=True,)
    news_per_page = models.IntegerField(max_length=50, help_text=_(u'Количество новостей на странице'))
    news_max_count = models.IntegerField(max_length=50, help_text=_(u'Количество новостей на всех страницах'))

    def __unicode__(self):
        return self.greeting_page.choise

class GreetingPageOption(models.Model):
    choise = models.CharField(max_length=14)

    def __unicode__(self):
        return self.choise


class Cheat(models.Model):
    enable_cheats = models.BooleanField(default=False)
    cheating_registered_users = models.CharField(max_length=100, default=0, blank=True)
    cheating_characters = models.CharField(max_length=100, default=0, blank=True)

    def __unicode__(self):
        return self.cheating_registered_users