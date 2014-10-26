# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_room_retgion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_retgion',
            new_name='room_region_id',
        ),
    ]
