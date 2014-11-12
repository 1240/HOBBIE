# -*- coding: utf-8 -*-
import datetime

from django.db import models


# Create your models here.
from mainpage.models import Regions
from django.utils import timezone


class Room(models.Model):
    class Meta():
        db_table = 'room'

    room_title = models.CharField(max_length=100, verbose_name="Название комнаты (краткое описание вашего предложения)")
    room_text = models.TextField(verbose_name="Описание комнаты")
    hash_tags = models.TextField(verbose_name="Ключевые слова - для того, чтобы людям было проще найти вашу комнату (укажите через пробел)", blank=True, null=True)
    room_create_date = models.DateTimeField(default=timezone.now)
    room_to_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата мероприятия (указывать не обязательно)")
    room_people_count = models.IntegerField(default=1)
    room_region = models.ForeignKey(Regions)
    room_open = models.BooleanField(default=True, verbose_name="Открытая/закрытая комната")
    room_image = models.CharField(null=True, blank=True, max_length=100, verbose_name="Изображение комнаты")



class Category(models.Model):
    class Meta():
        db_table = 'category'

    category_title = models.CharField(max_length=40)
    category_room_count = models.IntegerField(default=0)
    category_image = models.ImageField(upload_to='images/category_images/', blank=True, null=True)
    category_rooms = models.ManyToManyField(Room, through='CategoryRooms', null=True)

class RoomImage(models.Model):
    class Meta():
        db_table = 'roomimage'

    roomimage_image = models.ImageField(upload_to='images/category_images/', blank=True, null=True)
    roomimage_category = models.ForeignKey(Category)

class CategoryRooms(models.Model):
    room = models.ForeignKey(Room)
    category = models.ForeignKey(Category)

