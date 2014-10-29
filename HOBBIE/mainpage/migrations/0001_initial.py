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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('city_name', models.CharField(verbose_name='Название города', max_length=100)),
                ('city_id', models.CharField(verbose_name='ИД города', max_length=100)),
                ('city_title', models.CharField(verbose_name='Заголовок', max_length=100)),
                ('city_url', models.CharField(verbose_name='Ссылка', max_length=100)),
            ],
            options={
                'db_table': 'cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('region_name', models.CharField(verbose_name='Название области', max_length=100)),
                ('region_id', models.CharField(verbose_name='ИД региона', max_length=100)),
                ('region_title', models.CharField(verbose_name='Заголовок', max_length=100)),
                ('region_url', models.CharField(verbose_name='Ссылка', max_length=100)),
                ('is_west', models.BooleanField(verbose_name='Западная часть?', default=True)),
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
