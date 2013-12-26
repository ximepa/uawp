# -*- coding: utf-8 -*-
__author__ = 'ximepa'
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from cabinet.models import UserProfile
from web.models import NewsGroups
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from captcha.fields import CaptchaField


class NewsGroupForm(forms.Form):
    groups = forms.ModelChoiceField(queryset=NewsGroups.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'selectpicker'}),)


class CaptchaRegistrationForm(RegistrationForm, forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #captcha = CaptchaField(label=_('Captcha'))

class CaptchaAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label=_('Captcha'),)

class CaptchaPasswordChangeForm(PasswordChangeForm):
    captcha = CaptchaField(label=_('Captcha'))

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _(u'Введите старый пароль')}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _(u'Введите новый пароль')}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _(u'Повторите новый пароль')}))