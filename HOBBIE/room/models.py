# -*- coding: utf-8 -*-
import datetime

from django.db import models


# Create your models here.
from mainpage.models import Regions


class Room(models.Model):
    class Meta():
        db_table = 'room'

    room_title = models.CharField(max_length=100, verbose_name="Название комнаты")
    room_text = models.TextField(verbose_name="Описание комнаты")
    room_create_date = models.DateTimeField(default=datetime.datetime.now)
    room_to_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата удаления комнаты")
    room_people_count = models.IntegerField(default=1)
    room_region = models.ForeignKey(Regions)
    room_open = models.BooleanField(default=True,verbose_name="Открытая/закрытая комната")
    room_image = models.CharField(null=True, blank=True, max_length=100, verbose_name="Изображение комнаты")


class Message(models.Model):
    class Meta():
        db_table = 'message'

    message_text = models.TextField(verbose_name="Текст сообщения")
    message_datetime = models.DateTimeField(default=datetime.datetime.now)
    message_room = models.ForeignKey(Room)