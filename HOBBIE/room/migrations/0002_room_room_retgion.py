# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_retgion',
            field=models.ForeignKey(default=1, to='mainpage.Regions'),
            preserve_default=False,
        ),
    ]
