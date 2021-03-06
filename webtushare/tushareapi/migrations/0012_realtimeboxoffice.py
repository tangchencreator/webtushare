# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-08 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tushareapi', '0011_auto_20171023_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealTimeBoxOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_office', models.FloatField(verbose_name='\u5b9e\u65f6\u7968\u623f\uff08\u4e07\uff09')),
                ('irank', models.IntegerField(verbose_name='\u6392\u540d')),
                ('movie_name', models.CharField(max_length=300, verbose_name='\u5f71\u7247\u540d')),
                ('box_per', models.FloatField(verbose_name='\u7968\u623f\u5360\u6bd4 \uff08%\uff09')),
                ('movie_day', models.IntegerField(verbose_name='\u4e0a\u6620\u5929\u6570')),
                ('sum_box_office', models.FloatField(verbose_name='\u7d2f\u8ba1\u7968\u623f\uff08\u4e07\uff09')),
                ('time', models.TimeField(verbose_name='\u6570\u636e\u83b7\u53d6\u65f6\u95f4')),
            ],
        ),
    ]
