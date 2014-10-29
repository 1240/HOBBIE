from django.conf.urls import url, patterns

__author__ = '1240'

urlpatterns = patterns('',
    url(r'^$', 'mainpage.views.home', name="Главная"),
    url(r'^main_west/', 'mainpage.views.main_west', name="Главная"),
    url(r'^main_east/', 'mainpage.views.main_east', name="Главная"),
)