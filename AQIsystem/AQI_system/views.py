# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import Users,Daydata
from django.core.paginator import Paginator
# Create your views here.
def daytime(request):
    limit = 8
    daytimedatas = Daydata.objects.all().order_by('-id')
    pag = Paginator(daytimedatas, limit)
    page = request.GET.get('page', 1)
    loaded = pag.page(page)
    return render(request,'blogs.html',{'daytimedatas':loaded})

def datadetails(request, id):
    return render(request,'blog.html')


