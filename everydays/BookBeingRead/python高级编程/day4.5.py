# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/3 20:26
# FileName : day4.5
# Description : 描述符和属性
# --------------------------------

class MyClass(object):

    __secret_value = 1

# instance = MyClass()
# print(instance._secret_value)

class MyClass2(object):

    def __init__(self):
        # self.__private_value = 1
        self._private_value = 1

instance = MyClass2()
print(instance._private_value)


