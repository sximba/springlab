from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'springlab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^video/', include('ytv.urls', namespace='ytv')),
    url(r'^admin/', include(admin.site.urls)),
)
