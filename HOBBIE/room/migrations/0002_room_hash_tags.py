# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='hash_tags',
            field=models.TextField(blank=True, verbose_name='Хтег', null=True),
            preserve_default=True,
        ),
    ]
