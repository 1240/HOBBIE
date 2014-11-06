# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_message_message_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('category_title', models.CharField(max_length=40)),
                ('category_room_count', models.IntegerField(default=0)),
                ('category_image', models.ImageField(null=True, blank=True, upload_to='images/category_images/')),
            ],
            options={
                'db_table': 'category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('category', models.ForeignKey(to='room.Category')),
                ('room', models.ForeignKey(to='room.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='category_rooms',
            field=models.ManyToManyField(null=True, through='room.CategoryRooms', to='room.Room'),
            preserve_default=True,
        ),
    ]
