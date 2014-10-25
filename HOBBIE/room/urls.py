from django.conf.urls import url, patterns

__author__ = '1240'

urlpatterns = patterns('',
    url(r'^rooms/all/$', 'room.views.rooms'),
    url(r'^rooms/get/(?P<room_id>\d+)/$', 'room.views.room'),
    url(r'^rooms/addmessage/(?P<room_id>\d+)/$', 'room.views.addmessage'),
    url(r'^$', 'mainpage.views.home'),
    url(r'^rooms/makeroom/$', 'room.views.makeroom'),
    url(r'^rooms/addroom/$', 'room.views.addroom'),
    url(r'^rooms/join/(?P<room_id>\d+)/$', 'room.views.joinroom'),
    url(r'^rooms/invite/(?P<room_id>\d+)/$', 'room.views.invite'),
)