# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/17 20:56
# FileName : day10.2
# Description : 单列模式
# --------------------------------
class Signleton(object):
    def __new__(cls, *args, **kwargs):
        try:
            ob = getattr(cls,'_instance')
            print(ob)
        except:
            print("it is no object")
        if not hasattr(cls,'_instance'):
            orig = super(Signleton,cls)
            cls._instance = orig.__new__(cls,*args,**kwargs)
        print(cls._instance)
        return cls._instance

class MyClass(Signleton):
    a = 1

# class MyOtherClass(MyClass):
#     b = 2


one = MyClass()
print('one',one)
two = MyClass()
print('two',two)
two.a = 3
print(one.a)

