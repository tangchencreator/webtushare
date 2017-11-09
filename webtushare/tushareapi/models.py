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

class ReportData(models.Model):
    '''
    业绩报告
    code,代码
    name,名称
    esp,每股收益
    eps_yoy,每股收益同比(%)
    bvps,每股净资产
    roe,净资产收益率(%)
    epcf,每股现金流量(元)
    net_profits,净利润(万元)
    profits_yoy,净利润同比(%)
    distrib,分配方案
    report_date,发布日期
    '''
    year = models.CharField("年份", max_length=4)
    quater = models.CharField("季度", max_length=1)
    code = models.CharField("代码", max_length=7)
    name = models.CharField("名称", max_length=300)
    eps  = models.FloatField("每股收益", null=True)
    eps_yoy = models.FloatField("每股收益同比(%)", null=True)
    bvps = models.FloatField("每股净资产", null=True)
    roe = models.FloatField("净资产收益率(%)", null=True)
    epcf = models.FloatField("每股现金流量(元)", null=True)
    net_profits = models.FloatField("净利润(万元)", null=True)
    profits_yoy = models.FloatField("净利润同比(%)", null=True)
    distrib = models.CharField("分配方案", max_length=300, null=True)
    report_date = models.CharField("发布日期", max_length=8, null=True)

    def __str__(self):
        return "第" + self.year + "年 " + self.quater + "季度 业绩报告"

class OperationData(models.Model):
    '''
    营运能力
    code,代码
    name,名称
    arturnover,应收账款周转率(次)
    arturndays,应收账款周转天数(天)
    inventory_turnover,存货周转率(次)
    inventory_days,存货周转天数(天)
    currentasset_turnover,流动资产周转率(次)
    currentasset_days,流动资产周转天数(天)
    '''
    year = models.CharField("年份", max_length=4)
    quater = models.CharField("季度", max_length=1)
    code = models.CharField("代码", max_length=7)
    name = models.CharField("名称", max_length=300)
    arturnover = models.FloatField("应收账款周转率(次)")
    arturndays = models.FloatField("应收账款周转天数(天)")
    inventory_turnover = models.FloatField("存货周转率(次)")
    inventory_days = models.FloatField("存货周转天数(天)")
    currentasset_turnover = models.FloatField("流动资产周转率(次)")
    currentasset_days = models.FloatField("流动资产周转天数(天)")

    def __str__(self):
        return "第" + self.year + "年 " + self.quater + "季度 营运能力"

class ProfitData(models.Model):
    '''
    盈利能力
    code,代码
    name,名称
    roe,净资产收益率(%)
    net_profit_ratio,净利率(%)
    gross_profit_rate,毛利率(%)
    net_profits,净利润(万元)
    esp,每股收益
    business_income,营业收入(百万元)
    bips,每股主营业务收入(元)
    '''
    year = models.CharField("年份", max_length=4)
    quater = models.CharField("季度", max_length=1)
    code = models.CharField("代码", max_length=7)
    name = models.CharField("名称", max_length=300)
    roe = models.FloatField("净资产收益率(%)", null=True)
    net_profit_ratio = models.FloatField("净利率(%)", null=True)
    gross_profit_rate = models.FloatField("毛利率(%)", null=True)
    net_profits = models.FloatField("净利润(万元)", null=True)
    eps = models.FloatField("每股收益", null=True)
    business_income = models.FloatField("营业收入(百万元)", null=True)
    bips = models.FloatField("每股主营业务收入(元)", null=True)


class GrowthData(models.Model):
    '''
    成长能力
    code,代码
    name,名称
    mbrg,主营业务收入增长率(%)
    nprg,净利润增长率(%)
    nav,净资产增长率
    targ,总资产增长率
    epsg,每股收益增长率
    seg,股东权益增长率
    '''
    year = models.CharField("年份", max_length=4)
    quater = models.CharField("季度", max_length=1)
    code = models.CharField("代码", max_length=7)
    name = models.CharField("名称", max_length=300)
    mbrg = models.FloatField("主营业务收入增长率(%)")
    nprg = models.FloatField("净利润增长率(%)")
    nav = models.FloatField("净资产增长率")
    targ = models.FloatField("总资产增长率")
    epsg = models.FloatField("每股收益增长率")
    seg = models.FloatField("股东权益增长率")

class RealTimeBoxOffice(models.Model):
    '''
    BoxOffice 实时票房（万）
    Irank 排名
    MovieName 影片名
    boxPer 票房占比 （%）
    movieDay 上映天数
    sumBoxOffice 累计票房（万）
    time 数据获取时间
    '''
    box_office = models.FloatField("实时票房（万）")
    irank = models.IntegerField("排名")
    movie_name = models.CharField("影片名", max_length=300)
    box_per = models.FloatField("票房占比 （%）")
    movie_day = models.FloatField("上映天数")
    sum_box_office = models.FloatField("累计票房（万）")
    time = models.CharField("发布日期", max_length=20, null=True)

class DayBoxOffice(models.Model):
    '''
    AvgPrice 平均票价
    AvpPeoPle 场均人次
    BoxOffice 单日票房（万）
    BoxOffice_Up 环比变化 （%）
    IRank 排名
    MovieDay 上映天数
    MovieName 影片名
    SumBoxOffice 累计票房（万）
    WomIndex 口碑指数
    '''
    avg_price = models.FloatField("平均票价")
    avp_people = models.FloatField("场均人次")
    box_office = models.FloatField("单日票房（万）")
    box_office_up = models.FloatField("环比变化 （%）")
    irank = models.IntegerField("排名")
    movie_day = models.IntegerField("上映天数")
    movie_name = models.CharField("影片名", max_length=300)
    sum_box_office = models.FloatField("累计票房（万）")
    wom_index = models.FloatField("口碑指数", null=True, max_length=10)