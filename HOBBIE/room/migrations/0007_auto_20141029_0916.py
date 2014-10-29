# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_room_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_open',
            field=models.BooleanField(default=True, verbose_name='Открытая/закрытая комната'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_to_date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления комнаты'),
            preserve_default=True,
        ),
    ]
