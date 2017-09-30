from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tushareapi.models import StockBasic


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