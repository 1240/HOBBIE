# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('message_text', models.TextField(verbose_name='Текст сообщения')),
                ('message_datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'message',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('room_title', models.CharField(verbose_name='Название комнаты', max_length=100)),
                ('room_text', models.TextField(verbose_name='Описание комнаты')),
                ('room_create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('room_to_date', models.DateTimeField(null=True, blank=True, verbose_name='Дата мероприятия')),
                ('room_people_count', models.IntegerField(default=1)),
                ('room_open', models.BooleanField(default=True, verbose_name='Открытая/закрытая комната')),
                ('room_image', models.CharField(null=True, blank=True, verbose_name='Изображение комнаты', max_length=100)),
                ('room_region', models.ForeignKey(to='mainpage.Regions')),
            ],
            options={
                'db_table': 'room',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='message_room',
            field=models.ForeignKey(to='room.Room'),
            preserve_default=True,
        ),
    ]
