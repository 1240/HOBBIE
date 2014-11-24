# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_auto_20141113_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_create_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата создания комнаты'),
        ),
    ]
