# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext
from cabinet.models import Players, UserProfile
from django.utils.translation import gettext as _



# Create your views here.
def index(request):
    hello = 'hello'
    return render_to_response('index.html', {'hello': hello, 'user': request.user},
                                  context_instance=RequestContext(request))


def profile(request, ):
    characters = Players.objects.all()
    print characters
    print '----'
    if request.user.is_authenticated():
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            user_game_acc = user_profile.game_acc.all()
            user_acc_count = user_game_acc.count()
            user_characters = characters.filter(account_name__in = user_game_acc)
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


def profile_options(request):
    if request.user.is_authenticated():
        return render_to_response('cabinet/options.html', {'user': request.user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/accounts/login')