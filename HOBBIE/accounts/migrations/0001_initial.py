# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, unique=True, verbose_name='email', max_length=255)),
                ('username', models.CharField(unique=True, verbose_name='username', max_length=255)),
                ('avatar', models.ImageField(null=True, blank=True, verbose_name='Аватар', upload_to='images/%Y/%m/%d')),
                ('first_name', models.CharField(blank=True, verbose_name='Имя', max_length=255)),
                ('last_name', models.CharField(blank=True, verbose_name='Фамилия', max_length=255)),
                ('date_of_birth', models.DateField(null=True, blank=True, verbose_name='День рождения')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('friends', models.ManyToManyField(null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='friends_rel_+')),
                ('room', models.ManyToManyField(null=True, blank=True, to='room.Room')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
