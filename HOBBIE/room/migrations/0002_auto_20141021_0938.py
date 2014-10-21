# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_create_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_people_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_to_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
