# -*- coding: utf-8 -*-
__author__ = 'ximepa'
from django.views.static import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
urlpatterns = patterns('feed_back.views',

    url(r'^thanks/$', TemplateView.as_view(template_name='feedback/feedback_success.html')),
    url(r'^$', 'feedback', name='feedback'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)