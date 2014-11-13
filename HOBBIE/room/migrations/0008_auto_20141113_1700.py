# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_roomimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hash_tags',
            field=models.TextField(null=True, blank=True, verbose_name='Ключевые слова - для того, чтобы людям было проще найти вашу комнату (укажите через пробел)'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_title',
            field=models.CharField(max_length=100, verbose_name='Название комнаты (краткое описание вашего предложения)'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_to_date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Дата мероприятия (указывать не обязательно)'),
        ),
    ]
