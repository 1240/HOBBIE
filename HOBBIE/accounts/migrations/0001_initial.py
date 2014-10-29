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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('email', models.EmailField(unique=True, db_index=True, verbose_name='email', max_length=255)),
                ('username', models.CharField(unique=True, verbose_name='username', max_length=255)),
                ('avatar', models.ImageField(null=True, verbose_name='Аватар', blank=True, upload_to='images/%Y/%m/%d')),
                ('first_name', models.CharField(verbose_name='Имя', max_length=255, blank=True)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=255, blank=True)),
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
