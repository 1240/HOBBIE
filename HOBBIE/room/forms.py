# -*- coding: utf-8 -*-
from django.forms import ModelForm

from accounts.models import UserRoom

from room.models import Room


__author__ = '1240'


class MessageForm(ModelForm):
    class Meta():
        model = UserRoom
        fields = ['message_text']


class RoomForm(ModelForm):
    class Meta():
        model = Room
        fields = ['room_title', 'room_text', 'room_to_date', 'hash_tags']

