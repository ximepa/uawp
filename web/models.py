# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from tinymce.models import HTMLField
# Статичиские страницы


class StaticPages(models.Model):
    name = models.CharField(_(u'Cyrillic name'), max_length=20, unique=True, help_text=_(u'Page name for url. Example: donate'))
    page_name = models.CharField(max_length=20, verbose_name=_(u'Page name'), help_text=_(u'Page name'))
    title = models.CharField(max_length=100, verbose_name=_(u'Title'), blank=True, help_text=_(u'Page title'))
    text = HTMLField(help_text=_(u'Main text'))
    seo_title = models.CharField(max_length=20, verbose_name=_(u'Seo title'), blank=True, help_text=_(u'Title for search engine'))
    seo_description = models.CharField(max_length=20, verbose_name=_(u'Seo description'), blank=True, help_text=_(u'Desctiption for search engine'))
    seo_keyword = models.CharField(max_length=20, verbose_name=_(u'Seo keyword'), blank=True, help_text=_(u'Seo keyword for search engine'))
    author = models.ForeignKey(User, blank=True,)
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_(u'Created datetime'), help_text=_(u'Created date'))
    last_modified = models.DateTimeField(auto_now=True, verbose_name=_(u'Last modified'))
    show_in_menu = models.BooleanField(default=True, verbose_name=_(u'Show in menu'), help_text=_(u'Show page in menu on site'))

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('web:static_pages', [self.name])

    class Meta:
        verbose_name = _(u'Static page')
        verbose_name_plural = _(u'Static pages')


BOOTSTRAP_PANEL_CLASS = (
        ('primary', 'primary'),
        ('success', 'success'),
        ('info', 'info'),
        ('warning', 'warning'),
        ('danger', 'danger'),
        )


class NewsGroups(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    bootstrap_panel_class = models.CharField(choices=BOOTSTRAP_PANEL_CLASS, blank=True, max_length=100)

    def __unicode__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=100, verbose_name=_(u'Name'), blank=True, help_text=_(u'News name'))
    description = HTMLField(help_text=_(u'News description'))
    text = HTMLField(help_text=_(u'News main text'))
    group = models.ForeignKey(NewsGroups, blank=True)
    seo_title = models.CharField(max_length=20, verbose_name=_(u'Title'), blank=True, help_text=_(u'Title for search engine'))
    seo_description = models.CharField(max_length=20, verbose_name=_(u'Seo description'), blank=True, help_text=_(u'Desctiption for search engine'))
    seo_keyword = models.CharField(max_length=20, verbose_name=_(u'Seo keyword'), blank=True, help_text=_(u'Seo keyword for search engine'))
    show_news = models.BooleanField(default=True, verbose_name=_(u'Show news'), help_text=_(u'Show news on site'))
    author = models.ForeignKey(User, blank=True,)
    created = models.DateTimeField(verbose_name=_(u'Created datetime'), help_text=_(u'Time when was created'))
    last_modified = models.DateTimeField(auto_now=True, verbose_name=_(u'Last modified'), help_text=_(u'Time when was last modified'))

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('web:news', [self.id])

    class Meta:
        verbose_name = _(u'News')
        verbose_name_plural = _(u'News')
