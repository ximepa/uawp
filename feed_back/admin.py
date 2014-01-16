# -*- coding: utf-8 -*-
from django.contrib import admin
from feed_back.models import FeedBack, FeedBackGroup
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import ugettext_lazy as _


class FeedBackAdmin(admin.ModelAdmin):

    fieldsets = [
        (_(u'FeedBack:'), {'fields': (
            'group',
            'title',
            'name',
            'mail',
            'text',
        )})]
    list_display = ('id', 'group', 'title', 'name', 'mail', 'text')


class FeedBackGroupAdmin(admin.ModelAdmin):

    fieldsets = [
        (_(u'FeedBack:'), {'fields': (
            'name',
            'status',
        )})]
    list_display = ('id', 'name', 'status')


admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(FeedBackGroup, FeedBackGroupAdmin)
