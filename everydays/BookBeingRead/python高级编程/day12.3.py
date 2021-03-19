# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/18 14:14
# FileName : day12.3
# Description : 
# --------------------------------

class Obj(object):

    # def __str__(self):
    #     return self.__class__.__name__

    def __call__(self, event):
        print('__call__',event)
        return "__call__"

    def __repr__(self):
        print('__repr__')
        return self.__class__.__name__

    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super(Obj,cls).__new__(cls,*args, **kwargs)

    def __init__(self):
        print('__init__')

    def say(self):
        print("say...")

class A(object):

    def __str__(self):
        return self.__class__.__name__

ob = Obj()
print(ob)
ob(A())
