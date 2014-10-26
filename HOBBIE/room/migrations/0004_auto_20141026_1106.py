# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20141026_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_region_id',
            new_name='room_region',
        ),
    ]
