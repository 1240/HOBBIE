# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_auto_20141121_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hash_tags',
            field=models.CharField(null=True, max_length=200, blank=True, verbose_name='Ключевые слова - для того, чтобы людям было проще найти вашу комнату'),
            preserve_default=True,
        ),
    ]
