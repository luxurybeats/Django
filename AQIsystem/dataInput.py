#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AQIsystem.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()


def main():
    from AQI_system.models import Daydata
    import xlrd
    with xlrd.open_workbook('AQI2.xlsx') as data:
        print(u'开始导入数据')
        table = data.sheet_by_index(0)
        n = 1
        daydataworklist = []

        for line in range(n, table.nrows):
            row = table.row_values(line)
            daydataworklist.append(Daydata(
                AQI = row[0],
                Primary = row[1],
                SO2 = row[2],
                NO2 = row[3],
                PM10 = row[4],
                CO = row[5],
                O3 = row[6],
                PM2_5 = row[7],
                Time  = row[8],
            ))

        Daydata.objects.bulk_create(daydataworklist)


if __name__ == "__main__":
    main()
    print('Done!')