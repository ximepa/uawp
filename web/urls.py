# -*- coding: utf-8 -*-
__author__ = 'ximepa'
from django.views.static import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
urlpatterns = patterns('web.views',

    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^accounts/profile/change_game_pass/(?P<game_acc>.+)/', 'change_game_pass', name='change_game_pass'),
    #url(r'^accounts/profile/options/', 'profile_options', name='profile_options'),
    # url(r'^accounts/profile/bind_game_acc/', 'bind_game_acc', name='bind_game_acc'),
    # url(r'^accounts/profile/game_acc_success/', 'game_acc_success', name='game_acc_success'),
    # url(r'^accounts/profile/game_acc/', 'create_game_acc', name='create_game_acc'),
    #url(r'^accounts/profile/', 'profile', name='user_profile'),
    #(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^news/(?P<id>.+)/$', 'news_full', name='news_full'),
    url(r'^news/$', 'news', name='news'),
    url(r'^page/(?P<name>.+)/$', 'static_pages', name='static_pages'),
    #url(r'^countdown/$', 'countdown', name='countdown'),
    url(r'^$', 'index', name='index'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)