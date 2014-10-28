# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from mainpage.models import Regions
from room.models import Message, Room


__author__ = '1240'


class MessageForm(ModelForm):
    class Meta():
        model = Message
        fields = ['message_text']


class RoomForm(ModelForm):
    class Meta():
        model = Room
        fields = ['room_title', 'room_text', 'room_to_date','room_open']


