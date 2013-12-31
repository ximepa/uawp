# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext
from cabinet.models import Players, UserProfile, AccountData
from cabinet.forms import CreateGameAccountForm, ChangePasswordForm
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from uawp import settings
import hashlib
import base64


def profile(request, ):
    try:
        from uawp.settings import ENABLE_CABINET
    except ImportError:
        ENABLE_CABINET = True
        return ENABLE_CABINET
    if settings.ENABLE_CABINET:
        players = Players.objects.all()
        print players
        if request.user.is_authenticated():
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                print user_profile
                #user_game_acc = AccountData.objects.filter(profile=user_profile)
                #print user_game_acc
                user_acc_count = '2'
                user_characters = players.filter(account_id=1)
                print user_characters
                no_game_account = _(u'У вас нету игровых аккаутнов, чтобы создать новый аккаунт или привязать сущестующий, перейдите в настройки')
                if user_acc_count == 0:
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
        print 'eneble cabinet true'
        if request.user.is_authenticated():
            print 'user.is_authenticated'
            if request.method == 'POST':
                print 'request.method == POST'
                create_game_acc_form = CreateGameAccountForm(request.POST)
                account_name = request.POST.get('account_name')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                if create_game_acc_form.is_valid():
                    print 'create_game_acc_form.is_valid'
                    if password1 == password2:
                        print 'pass1 = pass2'
                        try:
                            print 'try'
                            user_profile = UserProfile.objects.get(user=request.user)
                            accounts = AccountData.objects.filter(user_profile=user_profile.id)
                            print accounts.count()
                            if accounts.count() <= settings.GAME_ACCOUNT_LIMIT:
                                print '<='
                                account = AccountData(name=create_game_acc_form.cleaned_data['account_name'])
                                account.password = base64.b64encode(hashlib.sha1(create_game_acc_form.cleaned_data['password1']).hexdigest().decode('hex'))
                                print account.password
                                account.activated = 1
                                account.access_level = 0
                                account.membership = 0
                                account.last_server = 0
                                account.credits = 0
                                account.user_profile = user_profile.id
                                print account.activated
                                account.save()
                                print account.pk
                                user_profile.game_acc.add(account)
                                return HttpResponseRedirect('/accounts/profile/game_acc_success/')
                            else:
                                print 'to many game account'
                        except UserProfile.DoesNotExist:
                            print 'profile not found'
                            #user_profile = UserProfile.objects.create(users=request.user)
                            #user_profile.save()
                            #saved_user_profile = UserProfile.objects.get(users=request.user)
                            #saved_user_profile.game_acc.add(login)
                    else:
                        print 'password did not much'
                else:
                    print 'form not valid'
            else:
                create_game_acc_form = CreateGameAccountForm()
            return render_to_response('cabinet/create_game_acc.html', {'form': create_game_acc_form, 'user': request.user, },
                                      context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/accounts/login')
    else:
        return render_to_response('404.html', {}, context_instance=RequestContext(request))


def game_acc_success(request):
    if request.user.is_authenticated():
        success = 'Успешно'
        return render_to_response('cabinet/game_acc_success.html', {'success': success, 'user': request.user})
    else:
        return HttpResponseRedirect('/accounts/login')


@login_required()
def change_game_pass(request, game_acc):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)
            try:
                account = AccountData.objects.get(name=game_acc)
                if account.check_password(request.POST['old_password']) and request.POST['new_password'] == request.POST['repeat_password']:
                    if form.is_valid():
                        account.password = base64.b64encode(hashlib.sha1(form.cleaned_data['new_password']).hexdigest().decode('hex'))
                        account.save()
                        return HttpResponseRedirect('/accounts/profile/game_acc_success/')
                    else:
                        raise ValidationError, 'форма неверна'
                else:
                    print 'Неверный старый пароль'
            except AccountData.DoesNotExist:
                print "Такого логине несуществует"
        else:
            form = ChangePasswordForm()
        return render_to_response('cabinet/change_game_pass.html',
                                  {'form': form, 'user': request.user,}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/accounts/login')