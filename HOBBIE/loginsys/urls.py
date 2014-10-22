from django.conf.urls import url, patterns

__author__ = '1240'

urlpatterns = patterns('',
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
)