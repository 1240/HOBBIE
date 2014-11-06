# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userroom_can_edit'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroom',
            name='message_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userroom',
            name='message_text',
            field=models.TextField(blank=True, verbose_name='Текст сообщения', null=True),
            preserve_default=True,
        ),
    ]
