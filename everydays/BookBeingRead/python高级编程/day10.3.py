# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/18 10:37
# FileName : day10.3
# Description : 这边只是共享了__dict__,不是单列模式
# --------------------------------

class Brog(object):
    _status = {}
    def __new__(cls, *args, **kwargs):
        ob = super(Brog,cls).__new__(cls,*args,**kwargs)
        print("111",ob)
        ob.__dict__ = cls._status
        print("222",ob)
        return ob

class MyClass(Brog):
    a = 1
    def __init__(self):
        self.c = 2

class MyOtherClass(Brog):
    b = 2


one = MyClass()
print('one',one)
two = MyClass()
print('two',two)
two.a = 3
two.c = 100
print(one.a)
print(one.c)



three = MyOtherClass()
print('three',three)
print(three.b)

