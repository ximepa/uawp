# -*- coding: utf-8 -*-
__author__ = 'ximepa'
from django.views.static import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
urlpatterns = patterns('cabinet.views',

    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #url(r'^accounts/profile/change_game_pass/(?P<game_acc>.+)/', 'change_game_pass', name='change_game_pass'),
    url(r'^profile/options/', 'profile_options', name='profile_options'),
    #url(r'^accounts/profile/bind_game_acc/', 'bind_game_acc', name='bind_game_acc'),
    #url(r'^accounts/profile/game_acc_success/', 'game_acc_success', name='game_acc_success'),
    #url(r'^accounts/profile/game_acc/', 'create_game_acc', name='create_game_acc'),
    url(r'^profile/', 'profile', name='user_profile'),
    url(r'^$', 'index', name='index'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)