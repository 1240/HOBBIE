# -*- coding: utf-8 -*-
from django import forms
from room.models import Message, Room
from django.forms import ModelForm, Form

__author__ = '1240'


class MessageForm(ModelForm):
    class Meta():
        model = Message
        fields = ['message_text']


class RoomForm(ModelForm):
    class Meta():
        model = Room
        fields = ['room_title', 'room_text', 'room_to_date']


