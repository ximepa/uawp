# -*- coding: utf-8 -*-

from django.db import models
from captcha.fields import CaptchaField
from django.utils.translation import gettext as _


class FeedBackGroup(models.Model):
    name = models.CharField(verbose_name=_('Название группы'), max_length=100)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группы')

    def __unicode__(self):
        return self.name


class FeedBack(models.Model):
    group = models.ForeignKey('FeedBackGroup')
    title = models.CharField(verbose_name=_('Тема:'), max_length=100)
    name = models.CharField(verbose_name=_('Имя:'), max_length=100, blank=True)
    mail = models.EmailField(verbose_name=_('Электронный адрес:'), max_length=100)
    text = models.TextField(verbose_name=_('Сообщение:'))

    class Meta:
        verbose_name = _('Сообщение')
        verbose_name_plural = _('Сообщения')

    def __unicode__(self):
        return self.title