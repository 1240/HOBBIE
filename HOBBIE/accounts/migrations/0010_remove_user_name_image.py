# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20141111_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name_image',
        ),
    ]
