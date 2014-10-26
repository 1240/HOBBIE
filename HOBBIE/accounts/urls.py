# -*- coding: utf-8 -*-
_author__ = '1240'
from django.conf.urls import url, patterns

__author__ = '1240'

urlpatterns = patterns('',
    url(r'^edit/', 'accounts.views.edit'),
    url(r'^(?P<username>\w+)/', 'accounts.views.user_page'),
)