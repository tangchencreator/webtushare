# -*-coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

'''
tushareapi 使用tushare对象 数据库存储对象
'''
__all__ = ['StockBasic']

class StockBasic(models.Model):
    '''
    获取沪深上市公司基本情况
    '''
    code = models.CharField("代码", max_length=7)
    name = models.CharField("名称", max_length=300)
    industry = models.CharField("所属行业", max_length=300)
    area = models.CharField("地区", max_length=300)
    pe = models.FloatField("市盈率")
    outstanding = models.FloatField("流通股本(亿)")
    totals = models.FloatField("总股本(亿)")
    totalAssets = models.FloatField("总资产(万)")
    liquidAssets = models.FloatField("流动资产")
    fixedAssets = models.FloatField("固定资产")
    reserved = models.FloatField("公积金")
    reservedPerShare = models.FloatField("每股公积金")
    esp = models.FloatField("每股收益")
    bvps = models.FloatField("每股净资")
    pb = models.FloatField("市净率")
    timeToMarket = models.CharField("上市日期", max_length=8)
    undp = models.FloatField("未分利润")
    perundp = models.FloatField("每股未分配")
    rev = models.FloatField("收入同比(%)")
    profit = models.FloatField("利润同比(%)")
    gpr = models.FloatField("毛利率(%)")
    npr = models.FloatField("净利润率(%)")
    holders = models.IntegerField("股东人数")

    def __str__(self):
        return self.name


