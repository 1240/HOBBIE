# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
        ('accounts', '0002_auto_20141102_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_creator', models.BooleanField(default=False)),
                ('room', models.ForeignKey(to='room.Room')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='room',
        ),
        migrations.AddField(
            model_name='user',
            name='room2',
            field=models.ManyToManyField(through='accounts.UserRoom', null=True, to='room.Room'),
            preserve_default=True,
        ),
    ]
