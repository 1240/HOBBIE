# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('room_title', models.CharField(max_length=100, verbose_name='Название комнаты')),
                ('room_text', models.TextField(verbose_name='Описание комнаты')),
                ('room_create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('room_to_date', models.DateTimeField(null=True, blank=True)),
                ('room_people_count', models.IntegerField(default=1)),
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
