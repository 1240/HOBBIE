from django.conf.urls import url, patterns

__author__ = '1240'

urlpatterns = patterns('',
    url(r'^1/', 'room.views.room_one', name="Комната №1"),
    url(r'^2/', 'room.views.template', name="Комната"),
    url(r'^$', 'room.views.home', name="Комнаты")
)