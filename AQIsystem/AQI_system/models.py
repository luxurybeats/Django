# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
# 创建数据库表
class Users(models.Model):
    username = models.CharField(max_length = 16)
    password = models.CharField(max_length = 16)
    address = models.TextField()
    email = models.EmailField()
    age = models.IntegerField()  
    def __unicode__(self):
        return self.username

class Daydata(models.Model):
    AQI = models.CharField(max_length = 16,null=True, blank=True)
    Primary  = models.CharField(u'首要污染物',max_length = 16, null=True, blank=True)
    SO2 =models.CharField(max_length = 16,null=True, blank=True)
    NO2 =models.CharField(max_length = 16,null=True, blank=True)
    PM10 = models.CharField(max_length = 16,null=True, blank=True)
    CO =models.CharField(max_length = 16,null=True, blank=True)
    O3 =models.CharField(max_length = 16,null=True, blank=True)
    PM2_5 = models.CharField(max_length = 16,null=True, blank=True)
    Time = models.CharField(max_length = 16)
    def __unicode__(self):
        return self.Time

class Dayindexdata(models.Model):
    AQI = models.CharField(max_length = 16)
    SO2 = models.CharField(max_length = 16)
    NO2 = models.CharField(max_length = 16)
    PM10 = models.CharField(max_length = 16)
    CO =models.CharField(max_length = 16)
    O3 =models.CharField(max_length = 16)
    PM2_5 = models.CharField(max_length = 16)

class Addressdata(models.Model):
    Time = models.CharField(max_length = 16)
    add1 = models.CharField(u'青羊区', max_length = 16)
    add2 = models.CharField(u'金牛区', max_length = 16)
    add3 = models.CharField(u'锦江区', max_length = 16)
    add4 = models.CharField(u'武侯祠', max_length = 16)
    add5 = models.CharField(u'成华区', max_length = 16)
    add6 = models.CharField(u'高新区', max_length = 16)
    add7 = models.CharField(u'龙泉驿区', max_length = 16)
    add8 = models.CharField(u'青白江区', max_length = 16)
    add9 = models.CharField(u'新都区', max_length = 16)
    add10 = models.CharField(u'温江区', max_length = 16)
    add11 = models.CharField(u'双流区', max_length = 16)
    add12 = models.CharField(u'郫县', max_length = 16)
    add13 = models.CharField(u'天府新区', max_length = 16)
    add14 = models.CharField(u'都江堰市', max_length = 16)
    add15 = models.CharField(u'崇州市', max_length = 16)
    add16 = models.CharField(u'新津县', max_length = 16)
    add17 = models.CharField(u'彭州市', max_length = 16)
    add18 = models.CharField(u'邛崃市', max_length = 16)
    add19 = models.CharField(u'大邑县', max_length = 16)
    add20 = models.CharField(u'蒲江县', max_length = 16)
    def __unicode__(self):
        return self.Time


class Daytimedata(models.Model):
    time_0_data = models.ForeignKey(Dayindexdata, related_name='time0' , verbose_name=u'0时')
    time_1_data = models.ForeignKey(Dayindexdata, related_name='time1' , verbose_name=u'1时')
    time_2_data = models.ForeignKey(Dayindexdata, related_name='time2' , verbose_name=u'2时')
    time_3_data = models.ForeignKey(Dayindexdata, related_name='time3' , verbose_name=u'3时')
    time_4_data = models.ForeignKey(Dayindexdata, related_name='time4' , verbose_name=u'4时')
    time_5_data = models.ForeignKey(Dayindexdata, related_name='time5' , verbose_name=u'5时')
    time_6_data = models.ForeignKey(Dayindexdata, related_name='time6' , verbose_name=u'6时')
    time_7_data = models.ForeignKey(Dayindexdata, related_name='time7' , verbose_name=u'7时')
    time_8_data = models.ForeignKey(Dayindexdata, related_name='time8' , verbose_name=u'8时')
    time_9_data = models.ForeignKey(Dayindexdata, related_name='time9' , verbose_name=u'9时')
    time_10_data = models.ForeignKey(Dayindexdata, related_name='time10' , verbose_name=u'10时')
    time_11_data = models.ForeignKey(Dayindexdata, related_name='time11' , verbose_name=u'11时')
    time_12_data = models.ForeignKey(Dayindexdata, related_name='time12' , verbose_name=u'12时')
    time_13_data = models.ForeignKey(Dayindexdata, related_name='time13' , verbose_name=u'13时')
    time_14_data = models.ForeignKey(Dayindexdata, related_name='time14' , verbose_name=u'14时')
    time_15_data = models.ForeignKey(Dayindexdata, related_name='time15' , verbose_name=u'15时')
    time_16_data = models.ForeignKey(Dayindexdata, related_name='time16' , verbose_name=u'16时')
    time_17_data = models.ForeignKey(Dayindexdata, related_name='time17' , verbose_name=u'17时')
    time_18_data = models.ForeignKey(Dayindexdata, related_name='time18' , verbose_name=u'18时')
    time_19_data = models.ForeignKey(Dayindexdata, related_name='time19' , verbose_name=u'19时')
    time_20_data = models.ForeignKey(Dayindexdata, related_name='time20' , verbose_name=u'20时')
    time_21_data = models.ForeignKey(Dayindexdata, related_name='time21' , verbose_name=u'21时')
    time_22_data = models.ForeignKey(Dayindexdata, related_name='time22' , verbose_name=u'22时')
    time_23_data = models.ForeignKey(Dayindexdata, related_name='time23' , verbose_name=u'23时')


class Addressdaytimedata(models.Model):
    address1 = models.ForeignKey(Daytimedata,related_name='add1' , verbose_name=u'成都市')
    address2 = models.ForeignKey(Daytimedata,related_name='add2' , verbose_name=u'君平街')
    address3 = models.ForeignKey(Daytimedata,related_name='add3' , verbose_name=u'大石西路')
    address4 = models.ForeignKey(Daytimedata,related_name='add4' , verbose_name=u'梁家巷')
    address5 = models.ForeignKey(Daytimedata,related_name='add5' , verbose_name=u'金泉两河')
    address6 = models.ForeignKey(Daytimedata,related_name='add6' , verbose_name=u'沙河滩')
    address7 = models.ForeignKey(Daytimedata,related_name='add7' , verbose_name=u'三瓦窑')
    address8 = models.ForeignKey(Daytimedata,related_name='add8' , verbose_name=u'十里店')
    address9 = models.ForeignKey(Daytimedata,related_name='add9' , verbose_name=u'灵岩山')


class Daytime(models.Model):
    time = models.ForeignKey(Addressdaytimedata, verbose_name=u'时间')




