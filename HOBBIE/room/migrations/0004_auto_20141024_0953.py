# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20141021_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_text',
            field=models.TextField(verbose_name='Текст сообщения'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_text',
            field=models.TextField(verbose_name='Описание комнаты'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_title',
            field=models.CharField(max_length=100, verbose_name='Название комнаты'),
        ),
    ]
