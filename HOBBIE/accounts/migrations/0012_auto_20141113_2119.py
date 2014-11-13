# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_geoip', '0001_initial'),
        ('accounts', '0011_userroom_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.ForeignKey(to='django_geoip.Region', default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
