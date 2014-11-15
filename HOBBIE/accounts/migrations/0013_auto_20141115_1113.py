# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20141113_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.ForeignKey(to='mainpage.Regions'),
        ),
    ]
