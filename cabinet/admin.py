# -*- coding: utf-8 -*-
from django.contrib import admin
from cabinet.models import Players, PlayerAppearance, AccountData, UserProfile
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import ugettext_lazy as _
from django import forms


class PlayersAdmin(admin.ModelAdmin):

    fieldsets = [
        (_(u'Options:'), {'fields': (
            'name',
            'account',
            'account_name',
            'exp',
            'recoverexp',
            'x',
            'y',
            'z',
            'heading',
            'world_id',
            'gender',
            'race',
            'player_class',
            'creation_date',
            'deletion_date',
            'last_online',
            'cube_size',
            'advanced_stigma_slot_size',
            'warehouse_size',
            'mailboxletters',
            'brokerkinah',
            'bind_point',
            'title_id',
            'online',
            'note',
            'repletionstate',
            'bg_points',
            'personal_rating',
            'arena_points',
            'partner_id',
        )})]
    list_display = ('id', 'name', 'account', 'account_name')


class AccountDataAdmin(admin.ModelAdmin):

    fieldsets = [
        (_(u'Options:'), {'fields': (
            'user_profile',
            'name',
            'password',
            'activated',
            'access_level',
            'membership',
            'last_server',
            'last_ip',
            'last_mac',
            'ip_force',
            'credits',
            'email',
            'last_logout',
        )})]
    list_display = ('name', 'password', 'activated', 'access_level')


class AccountDataInline(admin.TabularInline):
    model = AccountData
    fk_name = 'user_profile'
    max_num = 5
    exclude = ('password',)


class UserProfileAdmin(admin.ModelAdmin):

    inlines = [
        AccountDataInline,
    ]


    fieldsets = [
        (_(u'Options:'), {'fields': (
            'user',
            'coints',
            'is_premium',
            'is_vip',
            'premium_start',
            'premium_end',
        )})]
    list_display = ('id', 'user', 'coints', 'is_premium', 'is_vip', 'premium_start', 'premium_end')



admin.site.register(Players, PlayersAdmin)
admin.site.register(AccountData, AccountDataAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
