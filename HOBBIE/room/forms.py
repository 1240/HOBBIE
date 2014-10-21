# -*- coding: utf-8 -*-
from room.models import Message
from django.forms import ModelForm

__author__ = '1240'


class MessageForm(ModelForm):
    class Meta():
        model = Message
        fields = ['message_text']



