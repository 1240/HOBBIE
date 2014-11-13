# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_user_name_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroom',
            name='invite',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
