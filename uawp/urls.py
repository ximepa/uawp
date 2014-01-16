from django.conf.urls import patterns, include, url
from django.contrib import admin
from cabinet.forms import CaptchaAuthenticationForm, CaptchaRegistrationForm
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uawp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^captcha/', include('captcha.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', 'authentication_form':CaptchaAuthenticationForm}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logged_out.html'}, ),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^feedback/$', include('feed_back.urls', 'feed_back')),
    url(r'^accounts/', include('cabinet.urls', 'cabinet')),
    url(r'^', include('web.urls', 'web')),
    url(r'^admin/', include(admin.site.urls)),
)
