# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_auto_20141026_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_open',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
