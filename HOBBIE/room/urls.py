from dajaxice.core import dajaxice_config
from django.conf.urls import url, patterns, include

__author__ = '1240'

urlpatterns = patterns('',
                       url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
                       url(r'^rooms/get/(?P<room_id>\d+)/$', 'room.views.room'),
                       # url(r'^rooms/addmessage/(?P<room_id>\d+)/$', 'room.views.addmessage'),
                       url(r'^$', 'mainpage.views.home'),
                       url(r'^rooms/makeroom/$', 'room.views.makeroom'),
                       url(r'^rooms/addroom/$', 'room.views.addroom'),
                       url(r'^rooms/join/(?P<room_id>\d+)/$', 'room.views.joinroom'),
                       url(r'^rooms/invite/(?P<room_id>\d+)/$', 'room.views.invite'),
                       url(r'^rooms/leave/(?P<room_id>\d+)/$', 'room.views.leave'),
                       url(r'^rooms/editroom/(?P<room_id>\d+)/$', 'room.views.editroom'),
                       url(r'^rooms/(?P<region_name>\w+)/$', 'room.views.rooms'),

)