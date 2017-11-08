from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tushareapi.models import StockBasic, ReportData, OperationData, ProfitData, RealTimeBoxOffice


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class StockBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockBasic
        fields = ('code', 'name', 'industry', 'area', 'pe', 'outstanding', 'totals', \
                  'totalAssets', 'liquidAssets', 'fixedAssets', 'reserved', 'reservedPerShare', \
                  'esp', 'bvps', 'pb', 'timeToMarket', 'undp', 'perundp', 'rev', 'profit', \
                  'gpr', 'npr', 'holders')

class ReportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportData
        fields = ('code', 'name', 'eps', 'eps_yoy', 'bvps', 'roe', 'epcf', \
                  'net_profits', 'profits_yoy', 'distrib', 'report_date')

class OperationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationData
        fields = ('code', 'name', 'arturnover', 'arturndays', 'inventory_turnover', \
                 'inventory_days', 'currentasset_turnover', 'currentasset_days')

class ProfitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfitData
        fields = ('code', 'name', 'roe', 'net_profit_ratio', 'gross_profit_rate', \
                 'net_profits', 'eps', 'bips')

class RealTimeBoxOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealTimeBoxOffice
        fields = ('box_office', 'irank', 'movie_name', 'box_per', 'movie_day', \
                 'sum_box_office', 'time')