# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_auto_20141106_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('roomimage_image', models.ImageField(blank=True, null=True, upload_to='images/category_images/')),
                ('roomimage_category', models.ForeignKey(to='room.Category')),
            ],
            options={
                'db_table': 'roomimage',
            },
            bases=(models.Model,),
        ),
    ]
