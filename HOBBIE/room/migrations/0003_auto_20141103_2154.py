# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_hash_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hash_tags',
            field=models.TextField(verbose_name='#Tags (укажите через пробел)', null=True, blank=True),
        ),
    ]
