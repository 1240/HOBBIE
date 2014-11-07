# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20141106_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, verbose_name='Аватар', default='images/avatar.jpg', null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar_chat',
            field=models.ImageField(blank=True, default='images/avatar.jpg', null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='main_avatar',
            field=models.ImageField(blank=True, default='images/avatar.jpg', null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
