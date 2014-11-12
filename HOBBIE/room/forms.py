# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea, DateTimeInput
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
        widgets = {
            'hash_tags': Textarea(attrs={'cols': 1, 'rows': 1}),
            'room_to_date': DateTimeInput(attrs={'readonly': 1}),
        }
