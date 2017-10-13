# -*- coding:utf-8 -*-
from django import forms

#获取表单数据方法
class AddForm(forms.Form):
    username = forms.CharField(max_length = 16)
    password = forms.CharField(max_length = 16)
    address = forms.CharField(max_length = 16)
    email = forms.EmailField()
    age = forms.IntegerField()
