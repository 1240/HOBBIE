# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0010_auto_20141124_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('hash_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
