# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('city_name', models.CharField(max_length=100, verbose_name='Название города')),
                ('city_id', models.CharField(max_length=100, verbose_name='ИД города')),
                ('city_title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('city_url', models.CharField(max_length=100, verbose_name='Ссылка')),
            ],
            options={
                'db_table': 'cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('region_name', models.CharField(max_length=100, verbose_name='Название области')),
                ('region_id', models.CharField(max_length=100, verbose_name='ИД региона')),
                ('region_title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('region_url', models.CharField(max_length=100, verbose_name='Ссылка')),
            ],
            options={
                'db_table': 'regions',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cities',
            name='city_region',
            field=models.ForeignKey(to='mainpage.Regions'),
            preserve_default=True,
        ),
    ]
