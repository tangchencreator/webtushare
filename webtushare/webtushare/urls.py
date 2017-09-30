# -*-coding:utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from tushareapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
##基本面数据
#沪深股票列表

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tushareapi/', include('tushareapi.urls')),
]
