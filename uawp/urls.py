from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uawp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^captcha/', include('captcha.urls')),
    (r'^tinymce/', include('tinymce.urls')),

    url(r'^', include('web.urls', 'web')),
    url(r'^admin/', include(admin.site.urls)),
)
