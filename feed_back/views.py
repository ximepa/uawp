# -*- coding: utf-8 -*-
from django.shortcuts import render
from feed_back.forms import FeedbackForm
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response, render

def feedback(request):
    print FeedbackForm()
    if request.method == 'POST':
        print request.POST
        print request.user
        feedback_form = FeedbackForm(request.POST or None)
        if feedback_form.is_valid():
            print 'valid'
            feedback_form.username = request.user
            groups = feedback_form.cleaned_data['groups']
            topic = feedback_form.cleaned_data['topic']
            username = request.user
            email = feedback_form.cleaned_data['email']
            message = feedback_form.cleaned_data['message']
            return HttpResponseRedirect('thanks/')
        else:
            print 'not valid'
    else:
        feedback_form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {
        'form': feedback_form,
    })