# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20141106_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_chat',
            field=models.ImageField(default='/media/images/avatar.jpg', upload_to='images/%Y/%m/%d', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='main_avatar',
            field=models.ImageField(default='/media/images/avatar.jpg', upload_to='images/%Y/%m/%d', null=True, blank=True),
            preserve_default=True,
        ),
    ]
