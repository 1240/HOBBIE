# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name_image',
            field=models.ImageField(upload_to='images/name_image/%Y/%m/%d', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='username_image',
            field=models.ImageField(upload_to='images/username_image/%Y/%m/%d', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(verbose_name='Аватар', default='/media/images/avatar.jpg', blank=True, upload_to='images/%Y/%m/%d', null=True),
        ),
    ]
