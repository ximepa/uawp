# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext
from cabinet.models import Players, UserProfile
from cabinet.forms import CreateGameAccountForm
from django.utils.translation import gettext as _
from uawp import settings



# Create your views here.
def profile(request, ):
    try:
        from uawp.settings import ENABLE_CABINET
    except ImportError:
        ENABLE_CABINET = True
        return ENABLE_CABINET
    if settings.ENABLE_CABINET:
        players = Players.objects.all()
        if request.user.is_authenticated():
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                user_game_acc = user_profile.game_acc.all()
                user_acc_count = user_game_acc.count()
                user_characters = players.filter(account_name__in=user_game_acc)
                print user_characters
                no_game_account = _('У вас нету игровых аккаутнов, чтобы создать новый аккаунт или привязать сущестующий, перейдите в настройки')
                if user_game_acc.count() == 0:
                    return render_to_response('cabinet/profile.html', {
                        'no_game_account': no_game_account,
                        'user_acc_count': user_acc_count,
                        }, context_instance=RequestContext(request))
                else:
                    return render_to_response('cabinet/profile.html',
                                              {'user': request.user,
                                               'user_profile': user_profile, 'user_characters': user_characters, 'user_acc_count': user_acc_count}, context_instance=RequestContext(request))
            except UserProfile.DoesNotExist:
                return HttpResponseRedirect('/accounts/register/')
        else:
            return HttpResponseRedirect('/accounts/login')
    else:
        return render_to_response('404.html', {}, context_instance=RequestContext(request))


def profile_options(request):
    if settings.ENABLE_CABINET:
        if request.user.is_authenticated():
            return render_to_response('cabinet/options.html', {'user': request.user}, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/accounts/login')
    else:
        return render_to_response('404.html', {}, context_instance=RequestContext(request))


def bind_game_acc(request):
    pass


def create_game_acc(request):
    create_game_acc_form = CreateGameAccountForm()
    if settings.ENABLE_CABINET:
        if request.user.is_authenticated():
            if request.method == 'POST':
                create_game_acc_form = CreateGameAccountForm(request.POST)
                account_name = request.POST.get('account_name')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                if password1 == password2:

                    return render_to_response('cabinet/options.html', {'user': request.user}, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/accounts/login')
    else:
        return render_to_response('404.html', {}, context_instance=RequestContext(request))