# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Электропочта')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Ник')),
                ('avatar', models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, verbose_name='Аватар')),
                ('first_name', models.CharField(max_length=255, blank=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, blank=True, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(null=True, blank=True, verbose_name='День рождения')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
