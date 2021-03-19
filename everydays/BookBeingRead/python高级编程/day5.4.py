# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/4 17:44
# FileName : day5.4
# Description : 
# --------------------------------

class FirstClass(object):
    def _get_price(self):
        return '$500'
    def _get_the_price(self):
        return self._get_price()
    price = property(_get_the_price)

class SecondClass(FirstClass):
    def _get_price(self):
        return '$20'

    def _cheap_price(self):
        return '$10'
    price = property(_cheap_price)

first = FirstClass()
print(first.price)
second = SecondClass()
print(second.price)

