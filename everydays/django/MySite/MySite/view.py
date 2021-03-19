# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/4/15 20:59
# FileName : view
# Description : 
# --------------------------------

from django.http import HttpResponse
from django.shortcuts import render


def hello2(request):
    return HttpResponse("Hello world ! ")


def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)