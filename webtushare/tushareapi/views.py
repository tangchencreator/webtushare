# -*-coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from tushareapi.models import StockBasic
from rest_framework import viewsets
from tushareapi.serializers import UserSerializer, GroupSerializer, StockBasicSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import tushare as ts
import sys

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@csrf_exempt
def stockBasic_list(request):
    """
    沪深股票列表
    """
    if request.method == 'GET':
        queryset = StockBasic.objects.all()
        if not queryset :
            stockbasics = ts.get_stock_basics()
            total = len(stockbasics)
            percent = 0.0
            code = stockbasics.index
            value = stockbasics.values
            for i in range(0, len(stockbasics)):
                stockbasic = stockbasics.ix[i]
                StockBasic.objects.create(code = code[i],
                                        name = stockbasic['name'], \
                                        industry = stockbasic.industry, \
                                        area = stockbasic.area, \
                                        pe = stockbasic.pe, \
                                        outstanding = stockbasic.outstanding, \
                                        totals = stockbasic.totals, \
                                        totalAssets= stockbasic.totalAssets, \
                                        liquidAssets = stockbasic.liquidAssets, \
                                        fixedAssets = stockbasic.fixedAssets, \
                                        reserved = stockbasic.reserved, \
                                        reservedPerShare = stockbasic.reservedPerShare, \
                                        esp =  stockbasic.esp, \
                                        bvps = stockbasic.bvps, \
                                        pb = stockbasic.pb, \
                                        timeToMarket = stockbasic.timeToMarket, \
                                        undp = stockbasic.undp, \
                                        perundp = stockbasic.perundp, \
                                        rev = stockbasic.rev, \
                                        profit = stockbasic.profit, \
                                        gpr = stockbasic.gpr, \
                                        npr = stockbasic.npr, \
                                        holders = stockbasic.holders)
                percent = percent + 1
                hashes = '#' * int(percent/total * 50.0)
                spaces = ' ' * (50 - len(hashes))
                sys.stdout.write("\同步数据: [%s] %d%%" % (hashes + spaces, percent/total*100))
                sys.stdout.flush()
            
        serializer = StockBasicSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def stockBasic_detail(request, code):
    """
    股票信息
    code,代码
    name,名称
    industry,所属行业
    area,地区
    pe,市盈率
    outstanding,流通股本(亿)
    totals,总股本(亿)
    totalAssets,总资产(万)
    liquidAssets,流动资产
    fixedAssets,固定资产
    reserved,公积金
    reservedPerShare,每股公积金
    esp,每股收益
    bvps,每股净资
    pb,市净率
    timeToMarket,上市日期
    undp,未分利润
    perundp, 每股未分配
    rev,收入同比(%)
    profit,利润同比(%)
    gpr,毛利率(%)
    npr,净利润率(%)
    holders,股东人数
    """
    try:
        stockbasic = StockBasic.objects.get(code=code)
    except  StockBasic.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StockBasicSerializer(stockbasic)
        return JsonResponse(serializer.data)