# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20141115_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='images/avatar.jpg', verbose_name='Аватар', upload_to='images/%Y/%m/%d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.ForeignKey(to='mainpage.Regions', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
