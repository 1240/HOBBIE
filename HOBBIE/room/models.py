import datetime
from django.db import models

# Create your models here.


class Room(models.Model):
    class Meta():
        db_table = 'room'

    room_title = models.CharField(max_length=100)
    room_text = models.TextField()
    room_create_date = models.DateTimeField(default=datetime.datetime.now)
    room_to_date = models.DateTimeField(null=True, blank=True)
    room_people_count = models.IntegerField(default=1)


class Message(models.Model):
    class Meta():
        db_table = 'message'

    message_text = models.TextField()
    message_datetime = models.DateTimeField(default=datetime.datetime.now)
    message_room = models.ForeignKey(Room)