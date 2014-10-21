# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20141021_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
