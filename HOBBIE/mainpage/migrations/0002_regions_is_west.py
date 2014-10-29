# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regions',
            name='is_west',
            field=models.BooleanField(default='True', verbose_name='Западная часть?'),
            preserve_default=False,
        ),
    ]
