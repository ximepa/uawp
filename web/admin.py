# -*- coding: utf-8 -*-
from django.contrib import admin
from web.models import News, NewsGroups, StaticPages
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import ugettext_lazy as _
from django import forms


# Register your models here.
class NewsAdmin(TranslationAdmin):

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    class Media:
    #    css = {
    #        "all": ("my_styles.css",)
    #    }
        js = (
            'default/js/filter.js',
            'default/modeltranslation/js/force_jquery.js',
            'default/js/jquery-ui.min.js',
            'default/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('default/modeltranslation/css/tabbed_translation_fields.css',),
        }
    news_fields = ('name', 'description', 'text', 'group', 'seo_title', 'seo_description', 'seo_keyword', 'show_news', 'created',)

    fieldsets = [
        (_(u'Options:'), {'fields': news_fields}),
        ]
    list_display = ('name', 'description', 'text', 'group', 'seo_title', 'seo_description', 'seo_keyword', 'author', 'created', 'last_modified', 'show_news',)
    list_filter = ('show_news',)


class NewsGroupsAdmin(TranslationAdmin):
    class Media:
        js = (
            'default/js/filter.js',
            'default/modeltranslation/js/force_jquery.js',
            'default/js/jquery-ui.min.js',
            'default/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('default/modeltranslation/css/tabbed_translation_fields.css',),
        }

    fieldsets = [
        (_(u'Options:'), {'fields': ('name', 'bootstrap_panel_class', 'is_active',)}),
        ]
    list_display = ('name_ru', 'name_en', 'bootstrap_panel_class', 'is_active')


class StaticPagesAdmin(TranslationAdmin):

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    class Media:
    #    css = {
    #        "all": ("my_styles.css",)
    #    }
        js = (
            'default/js/filter.js',
            'default/modeltranslation/js/force_jquery.js',
            'default/js/jquery-ui.min.js',
            'default/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('default/modeltranslation/css/tabbed_translation_fields.css',),
        }

    static_fields = ('name', 'page_name', 'title', 'text', 'seo_title', 'seo_description', 'seo_keyword', 'show_in_menu')

    fieldsets = [
        (_(u'Options:'), {'fields': static_fields}),
        ]


admin.site.register(News, NewsAdmin)
admin.site.register(NewsGroups, NewsGroupsAdmin)
admin.site.register(StaticPages, StaticPagesAdmin)