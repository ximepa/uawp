# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _


class BindGameAccountForm(forms.Form):
    pass


class CreateGameAccountForm(forms.Form):
    account_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _(u'Введите старый пароль'), 'class': 'form-control'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _(u'Введите новый пароль'), 'class': 'form-control'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _(u'Повторите новый пароль'), 'class': 'form-control'}))