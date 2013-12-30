# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _


class BindGameAccountForm(forms.Form):
    pass


class CreateGameAccountForm(forms.Form):
    account_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))