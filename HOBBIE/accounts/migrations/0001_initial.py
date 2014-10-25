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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email', db_index=True)),
                ('username', models.CharField(unique=True, max_length=255, verbose_name='username')),
                ('avatar', models.ImageField(upload_to='images/%Y/%m/%d', null=True, verbose_name='Аватар', blank=True)),
                ('first_name', models.CharField(max_length=255, blank=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, blank=True, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(null=True, verbose_name='День рождения', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
