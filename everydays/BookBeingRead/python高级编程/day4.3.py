# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/3 19:34
# FileName : day4.3
# Description : 
# --------------------------------

class BaseBase(object):

    def __init__(self):
        object.__init__(self)

    def method(self):
        print("BaseBase")

class Base1(BaseBase):
    pass

class Base2(BaseBase):
    def method(self):
        print("Base2")

class MyClass(Base1,Base2):
    pass

def L(kclass):
    return [k.__name__ for k in kclass.__mro__]


here = MyClass()
here.method()

# print(L(MyClass))