from django.conf.urls import url, patterns

__author__ = '1240'

urlpatterns = patterns('',
    url(r'^$', 'mainpage.views.home', name="Главная"),
)