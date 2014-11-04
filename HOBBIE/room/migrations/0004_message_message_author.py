# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20141103_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_author',
            field=models.CharField(max_length=40, null=True),
            preserve_default=True,
        ),
    ]
