# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/5/18 15:12
# FileName : 2
# Description : 
# --------------------------------

class Singleton(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

a = Singleton.instance(1,2)
b = Singleton.instance(2,3)
print(a.x)
print(b.x)
print(id(a)==id(b))