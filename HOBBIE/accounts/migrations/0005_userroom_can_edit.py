# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20141103_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroom',
            name='can_edit',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
