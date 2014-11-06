# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_auto_20141106_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message_room',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
