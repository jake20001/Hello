# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/4 18:13
# FileName : day5.5
# Description : 
# --------------------------------

class Frozen(object):
    __slots__ = ['ice','cream']

class Normal(object):
    pass

print('__dict__' in dir(Frozen))
print('__slots__' in dir(Frozen))
print('__dict__' in dir(Normal))

print(dir(Frozen))