from django.conf.urls import patterns, url
from ytv import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^(?P<video_id>\d+)/$', views.destroy, name='destroy'),)
