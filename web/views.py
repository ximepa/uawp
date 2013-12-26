# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import gettext as _
from options.models import PageOption
from web.models import StaticPages, News, NewsGroups
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def index(request):
    hello = 'hello'
    return render_to_response('index.html', {'hello': hello, 'user': request.user},
                                  context_instance=RequestContext(request))


# Новости
def news(request):
    from django.utils import translation
    cur_language = translation.get_language()
    print cur_language
    page_options = PageOption.objects.get(pk=1)
    groups_all = NewsGroups.objects.all()
    if request.method == 'GET':
        request.session['groups'] = request.GET.get('groups', 0)
        group = request.session.get('groups', request.session.get('groups', 0))
    news_list = News.objects.all().order_by('-created')
    if group:
        news_list = news_list.filter(Q(group=group, show_news=True))[:page_options.news_max_count]
        print news_list
    if news_list.count() > 0:
        print(news_list.count())
        paginator = Paginator(news_list, page_options.news_per_page)
        page = request.GET.get('page')
        news_filter_form = NewsGroupForm()
        print news_filter_form
        try:
            if request.user.is_authenticated():
                news_status_true = paginator.page(page)
                return render_to_response('news.html', {
                    'news_filtered': news_status_true,
                    'user': request.user,
                    'news_filter_form': news_filter_form,
                    }, context_instance=RequestContext(request))
            else:
                news_status_true = paginator.page(page)
                return render_to_response('news.html', {'news_filtered': news_status_true, 'news_filter_form': news_filter_form,},
                                          context_instance=RequestContext(request))
        except PageNotAnInteger:
            if request.user.is_authenticated():
                news_status_true = paginator.page(1)
                return render_to_response('news.html', {'news_filtered': news_status_true, 'user': request.user, 'news_filter_form': news_filter_form,},
                                          context_instance=RequestContext(request))
            else:
                news_status_true = paginator.page(1)
                return render_to_response('news.html', {'news_filtered': news_status_true, 'news_filter_form': news_filter_form,},
                                          context_instance=RequestContext(request))
        except EmptyPage:
            if request.user.is_authenticated():
                news_status_true = paginator.page(paginator.num_pages)
                return render_to_response('news.html', {'news_filtered': news_status_true, 'user': request.user, },
                                          context_instance=RequestContext(request))
            else:
                news_status_true = paginator.page(paginator.num_pages)
                return render_to_response('news.html', {'news_filtered': news_status_true, },
                                          context_instance=RequestContext(request))
    else:
        print '404'
        return render_to_response('404.html', {'user': request.user},
                                  context_instance=RequestContext(request))

# полная новость
def news_full(request, id):
    if request.user.is_authenticated():
        if request.method == 'GET':
            try:
                full_news = News.objects.get(id=id, show_news=True)
                return render_to_response('news_full.html', {'full_news': full_news, 'user': request.user, }, context_instance=RequestContext(request))
            except News.DoesNotExist:
                return render_to_response('404.html', {'user': request.user, }, context_instance=RequestContext(request))
        else:
            return render_to_response('404.html', {'user': request.user, }, context_instance=RequestContext(request))
    else:
        if request.method == 'GET':
            try:
                full_news = News.objects.get(id=id, show_news=True)
                return render_to_response('news_full.html', {'full_news': full_news, }, context_instance=RequestContext(request))
            except News.DoesNotExist:
                return render_to_response('404.html', {})
        else:
            return render_to_response('404.html', {})


def static_pages(request, name):
    if request.user.is_authenticated():
        static_pages_true = Static_pages.objects.filter(show_in_menu=True)
        if request.method == 'GET':
            try:
                stat_pages = Static_pages.objects.get(name=name, show_in_menu=True)
                return render_to_response('static_pages.html',
                                          {'pages': stat_pages, 'pages_filtered': static_pages_true,
                                           'user': request.user, }, context_instance=RequestContext(request))
            except Static_pages.DoesNotExist:
                return render_to_response('404.html', {'pages_filtered': static_pages_true, 'user': request.user, },
                                          context_instance=RequestContext(request))
        else:
            return render_to_response('404.html', {'pages_filtered': static_pages_true, 'user': request.user, },
                                      context_instance=RequestContext(request))
    else:
        static_pages_true = Static_pages.objects.filter(show_in_menu=True)
        if request.method == 'GET':
            try:
                stat_pages = Static_pages.objects.get(name=name, show_in_menu=True)
                return render_to_response('static_pages.html',
                                          {'pages': stat_pages, 'pages_filtered': static_pages_true, },
                                          context_instance=RequestContext(request))
            except Static_pages.DoesNotExist:
                return render_to_response('404.html', {'pages_filtered': static_pages_true, },
                                          context_instance=RequestContext(request))
        else:
            return render_to_response('404.html', {'pages_filtered': static_pages_true, },
                                      context_instance=RequestContext(request))
