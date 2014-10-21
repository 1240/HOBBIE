# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('message_text', models.TextField()),
                ('message_datetime', models.DateTimeField()),
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
                ('room_title', models.CharField(max_length=100)),
                ('room_text', models.TextField()),
                ('room_create_date', models.DateTimeField()),
                ('room_to_date', models.DateTimeField()),
                ('room_people_count', models.IntegerField(default=0)),
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
