# -*-coding:utf-8 -*-
from django.conf.urls import url
import views

urlpatterns = [
    #基本面数据
    ##沪深股票列表
    url(r'^stockbasic/$', views.stockBasic_list),
    ##沪深股票
    url(r'^stockbasic/(?P<code>[0-9]+)/$', views.stockBasic_detail),
    ##业绩报告（主表）
    url(r'^reportdata/(?P<year>[0-9]+)/(?P<quater>[0-9]+)/$', views.reportdata_list),
    ##业绩报告明细
    url(r'^reportdata/(?P<year>[0-9]+)/(?P<quater>[0-9]+)/(?P<code>[0-9]+)/$', views.reportdata_detail),
    ##营运能力
    url(r'^profitdata/(?P<year>[0-9]+)/(?P<quater>[0-9]+)/$', views.profitdata_list),
    ##营运能力明细
    url(r'^profitdata/(?P<year>[0-9]+)/(?P<quater>[0-9]+)/(?P<code>[0-9]+)/$', views.operationdata_detail),

    #电影票房
    ##实时票房
    url(r'^realtimeboxoffice', views.realtimeboxoffice_list),
    ##每日票房
    url(r'^dayboxoffice', views.dayboxoffice_list),
]