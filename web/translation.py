# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from web.models import News, NewsGroups, StaticPages


class NewsGroupsTranslationOptions(TranslationOptions):
    fields = ('name',)


class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'text', 'seo_title', 'seo_description', 'seo_keyword',)


class StaticPagesTranslationOptions(TranslationOptions):
    fields = ('page_name', 'title', 'text', 'seo_title', 'seo_description', 'seo_keyword',)

translator.register(News, NewsTranslationOptions)
translator.register(NewsGroups, NewsGroupsTranslationOptions)
translator.register(StaticPages, StaticPagesTranslationOptions)