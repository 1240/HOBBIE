# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20141107_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar_chat',
        ),
        migrations.RemoveField(
            model_name='user',
            name='main_avatar',
        ),
    ]
