# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/4 18:22
# FileName : day6.1
# Description : 
# --------------------------------

class MyClass(object):

    def __new__(cls, *args, **kwargs):
        print('__new__ called')
        return object.__new__(cls)  # default factory

    def __init__(self):
        print('__init__ called')
        self.a = 1

# instance = MyClass()

class MyOtherClass(MyClass):
    def __init__(self):
        print('MyOther class __init__ called')
        super(MyOtherClass,self).__init__()
        self.b = 2

instance = MyOtherClass()


