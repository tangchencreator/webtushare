# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tushareapi', '0018_auto_20171109_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayboxoffice',
            name='wom_index',
            field=models.FloatField(max_length=10, null=True, verbose_name='\u53e3\u7891\u6307\u6570'),
        ),
    ]
