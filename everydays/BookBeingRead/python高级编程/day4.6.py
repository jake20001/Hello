# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/3 20:34
# FileName : day4.6
# Description : 
# --------------------------------

class UpperString(object):

    def __init__(self):
        self._value = ''

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if isinstance(value,str):
            self._value = value.upper()
        else:
            self._value = value

class MyClass(object):
    attribute = UpperString()


instance = MyClass()
print(instance.attribute)
instance.attribute = "my value"
print(instance.attribute)
instance.attribute = 11
print(instance.attribute)

# instance.__dict__ = {}
instance.new_att = 1
print(instance.__dict__)

instance.va = 2
print(instance.__dict__)