# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20141103_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='room2',
            new_name='room',
        ),
    ]
