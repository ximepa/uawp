from django import forms
from .models import FeedBack
from django.utils.translation import ugettext as _
from .models import FeedBackGroup
from captcha.fields import CaptchaField


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
    groups = forms.ModelChoiceField(queryset=FeedBackGroup.objects.all().order_by('name'), empty_label=None, widget=forms.Select(attrs={'class': 'selectpicker'}),)
    topic = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()