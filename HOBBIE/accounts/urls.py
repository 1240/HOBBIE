# -*- coding: utf-8 -*-
from dajaxice.core import dajaxice_config

_author__ = '1240'
from django.conf.urls import include
from django.conf.urls import url, patterns

__author__ = '1240'

urlpatterns = patterns('',
                       url(r'^users/$', 'accounts.views.users'),
                       url(r'^edit/', 'accounts.views.edit'),
                       url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
                       url(r'^friends/', 'accounts.views.friends'),
                       url(r'^rooms/', 'accounts.views.rooms'),
                       url(r'^(?P<username>\w+)/', 'accounts.views.user_page'),


)
