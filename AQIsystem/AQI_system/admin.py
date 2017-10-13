# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Users,Daytimedata, Addressdaytimedata, Daydata, Dayindexdata, Daytime

# Register your models here.
#创建超级管理员后台
admin.site.register(Users)
admin.site.register(Daydata)
admin.site.register(Dayindexdata)
admin.site.register(Daytimedata)
admin.site.register(Addressdaytimedata)
admin.site.register(Daytime)