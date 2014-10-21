from django.conf.urls import url, patterns

__author__ = '1240'

urlpatterns = patterns('',
    url(r'^1/', 'room.views.room_one'),
    url(r'^2/', 'room.views.template'),
    url(r'^3/', 'room.views.home'),
    url(r'^rooms/all/$', 'room.views.rooms'),
    url(r'^rooms/get/(?P<room_id>\d+)/$', 'room.views.room'),
)