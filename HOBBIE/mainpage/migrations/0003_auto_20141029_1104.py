# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_regions_is_west'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions',
            name='is_west',
            field=models.BooleanField(verbose_name='Западная часть?', default=True),
            preserve_default=True,
        ),
    ]
