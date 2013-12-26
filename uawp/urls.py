from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uawp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^captcha/', include('captcha.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logged_out.html'}, ),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^feedback/thanks/$', TemplateView.as_view(template_name='feedback/feedback_success.html')),
    url(r'^feedback/$', 'feed_back.views.feedback', name='feedback'),
    url(r'^accounts/', include('cabinet.urls', 'cabinet')),
    url(r'^', include('web.urls', 'web')),
    url(r'^admin/', include(admin.site.urls)),
)
