# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-23 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tushareapi', '0008_operationdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrowthData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='\u5e74\u4efd')),
                ('quater', models.CharField(max_length=1, verbose_name='\u5b63\u5ea6')),
                ('code', models.CharField(max_length=7, verbose_name='\u4ee3\u7801')),
                ('name', models.CharField(max_length=300, verbose_name='\u540d\u79f0')),
                ('mbrg', models.FloatField(verbose_name='\u4e3b\u8425\u4e1a\u52a1\u6536\u5165\u589e\u957f\u7387(%)')),
                ('nprg', models.FloatField(verbose_name='\u51c0\u5229\u6da6\u589e\u957f\u7387(%)')),
                ('nav', models.FloatField(verbose_name='\u51c0\u8d44\u4ea7\u589e\u957f\u7387')),
                ('targ', models.FloatField(verbose_name='\u603b\u8d44\u4ea7\u589e\u957f\u7387')),
                ('epsg', models.FloatField(verbose_name='\u6bcf\u80a1\u6536\u76ca\u589e\u957f\u7387')),
                ('seg', models.FloatField(verbose_name='\u80a1\u4e1c\u6743\u76ca\u589e\u957f\u7387')),
            ],
        ),
        migrations.CreateModel(
            name='ProfitData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='\u5e74\u4efd')),
                ('quater', models.CharField(max_length=1, verbose_name='\u5b63\u5ea6')),
                ('code', models.CharField(max_length=7, verbose_name='\u4ee3\u7801')),
                ('name', models.CharField(max_length=300, verbose_name='\u540d\u79f0')),
                ('roe', models.FloatField(verbose_name='\u51c0\u8d44\u4ea7\u6536\u76ca\u7387(%)')),
                ('net_profit_ratio', models.FloatField(verbose_name='\u51c0\u5229\u7387(%)')),
                ('gross_profit_rate', models.FloatField(verbose_name='\u6bdb\u5229\u7387(%)')),
                ('net_profits', models.FloatField(verbose_name='\u51c0\u5229\u6da6(\u4e07\u5143)')),
                ('esp', models.FloatField(verbose_name='\u6bcf\u80a1\u6536\u76ca')),
                ('business_income', models.FloatField(verbose_name='')),
                ('bips', models.FloatField(verbose_name='\u6bcf\u80a1\u4e3b\u8425\u4e1a\u52a1\u6536\u5165(\u5143)')),
            ],
        ),
    ]
