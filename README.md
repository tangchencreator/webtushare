基于 tushare，djangorestframework制作的财经数据网页端应用
tushare 请访问 http://tushare.org
djangorestframework 请访问 http://www.django-rest-framework.org

# 基本面数据
## 股票列表
### 公司基本情况
GET http://localhost:8000/tushareapi/stockbasic/
### 股票代码 600353 的公司基本情况
GET http://localhost:8000/tushareapi/stockbasic/600353

## 业绩报告
### 获取2014年第3季度的业绩报表数据
GET http://localhost:8000/tushareapi/reportdata/2014/3/
### 股票代码 001979 2014年第3季度的业绩报表数据
GET http://localhost:8000/tushareapi/reportdata/2014/3/001979

## 盈利能力
### 获取2014年第3季度的盈利能力数据
GET http://localhost:8000/tushareapi/profitdata/2014/3/
### 股票代码 001896 2014年第3季度的盈利能力数据
GET http://localhost:8000/tushareapi/profitdata/2014/3/001896
