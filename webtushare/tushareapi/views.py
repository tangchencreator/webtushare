# -*-coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from tushareapi.models import StockBasic, ReportData, OperationData, \
                              ProfitData
from rest_framework import viewsets
from tushareapi.serializers import UserSerializer, GroupSerializer, \
                                   StockBasicSerializer, ReportDataSerializer, \
                                   OperationDataSerializer, ProfitDataSerializer
                                   
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
    if request.method == 'GET':
        queryset = StockBasic.objects.all()
        if not queryset :
            stockbasics = ts.get_stock_basics()
            total = len(stockbasics)
            percent = 0.0
            code = stockbasics.index
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
                processbar(percent, total)
            
        serializer = StockBasicSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
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
    if request.method == 'GET':
        try:
            stockbasic = StockBasic.objects.get(code=code)
        except  StockBasic.DoesNotExist:
            return HttpResponse(status=404)

        serializer = StockBasicSerializer(stockbasic)
        return JsonResponse(serializer.data)

@csrf_exempt
def reportdata_list(request, year, quater):
    """
    业绩预告列表
    """
    reportdatas = None
    reportdatas = ReportData.objects.filter(year=year).filter(quater=quater)
    if not reportdatas :
        repdas = ts.get_report_data(int(year),int(quater))
        total = len(repdas)
        percent = 0.0
        repda = None
        
        for i in range(0, len(repdas)):
            percent = percent + 1
            try:
                    repda = repdas.ix[i]
                    ReportData.objects.create(year=year, \
                                            quater=quater, \
                                            code=repda.code, \
                                            name=repda['name'], \
                                            eps=repda.eps, \
                                            eps_yoy=repda.eps_yoy, \
                                            bvps=repda.bvps, \
                                            roe=repda.roe, \
                                            epcf=repda.epcf, \
                                            net_profits=repda.net_profits, \
                                            profits_yoy=repda.profits_yoy, \
                                            distrib=repda.distrib, \
                                            report_date = repda.report_date)
                    
                    processbar(percent, total)
            except:
                continue
    reportdatas = ReportData.objects.filter(year=year).filter(quater=quater)
    serializer = ReportDataSerializer(reportdatas, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def reportdata_detail(request, year, quater, code):
    if request.method == 'GET':
        try:
            report = ReportData.objects.filter(year=year).filter(quater=quater).filter(code=code)
        except  ReportData.DoesNotExist:
            return HttpResponse(status=404)

        serializer = ReportDataSerializer(report[0])
        return JsonResponse(serializer.data)

@csrf_exempt
def operationdata_list(request, year, quater):
    """
    营运能力列表
    """
    operations = OperationData.objects.filter(year=year).filter(quater=quater)
    if not operations :
        opers = ts.get_operation_data(int(year),int(quater))
        total = len(opers)
        percent = 0.0
        oper = None
        
        for i in range(0, len(opers)):
            percent = percent + 1
            try:
                    oper = opers.ix[i]
                    OperationData.objects.create(year=year, \
                                            quater=quater, \
                                            code=oper.code, \
                                            name=oper['name'], \
                                            arturnover=oper.arturnover, \
                                            arturndays=oper.arturndays, \
                                            inventory_turnover=oper.inventory_turnover, \
                                            inventory_days=oper.inventory_days, \
                                            currentasset_turnover=oper.currentasset_turnover, \
                                            currentasset_days=oper.currentasset_days)
                    
                    processbar(percent, total)
            except:
                continue
    operations = OperationData.objects.filter(year=year).filter(quater=quater)
    serializer = OperationDataSerializer(operations , many=True)
    return JsonResponse(serializer.data, safe=False)

def operationdata_detail(request, year, quater, code):
    if request.method == 'GET':
        try:
            report = OperationData.objects.filter(year=year).filter(quater=quater).filter(code=code)
        except  OperationData.DoesNotExist:
            return HttpResponse(status=404)

        serializer = OperationDataSerializer(report[0])
        return JsonResponse(serializer.data)

@csrf_exempt
def profitdata_list(request, year, quater):
    """
    盈利能力列表
    """
    details = ProfitData.objects.filter(year=year).filter(quater=quater)
    if not details :
        details = ts.get_profit_data(int(year),int(quater))
        total = len(details)
        percent = 0.0
        profit = None
        
        for i in range(0, total):
            percent = percent + 1
            detail = details.ix[i]
            ProfitData.objects.create(year=year, \
                                            quater=quater, \
                                            code=detail.code, \
                                            name=detail['name'], \
                                            roe=detail.roe, \
                                            net_profit_ratio=detail.net_profit_ratio, \
                                            gross_profit_rate=detail.gross_profit_rate, \
                                            net_profits=detail.net_profits, \
                                            eps=detail.eps, \
                                            business_income=detail.business_income, \
                                            bips=detail.bips)
                    
            processbar(percent, total)
    details = ProfitData.objects.filter(year=year).filter(quater=quater)
    serializer = ProfitDataSerializer(details , many=True)
    return JsonResponse(serializer.data, safe=False)

def profitdata_detail(request, year, quater, code):
    if request.method == 'GET':
        try:
            details = ProfitData.objects.filter(year=year).filter(quater=quater).filter(code=code)
        except  ProfitData.DoesNotExist:
            return HttpResponse(status=404)

        serializer = ProfitDataSerializer(details[0])
        return JsonResponse(serializer.data)

def processbar(percent, total):
    hashes = '#' * int(percent/total * 50.0)
    spaces = ' ' * (50 - len(hashes))
    sys.stdout.write(u"\r同步数据: [%s] %d%%" % (hashes + spaces, percent/total*100))
    if percent == total:
        print
    sys.stdout.flush()
    