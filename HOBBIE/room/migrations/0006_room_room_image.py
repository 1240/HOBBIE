# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_room_room_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_image',
            field=models.CharField(blank=True, null=True, verbose_name='Изображение комнаты', max_length=100),
            preserve_default=True,
        ),
    ]
