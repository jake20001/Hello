# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/4 19:07
# FileName : day6.2
# Description : 
# --------------------------------

def method(self):
    return 1

klass = type('MyClass',(object,),{'method':method})
instance = klass()
# print(getattr('MyClass','method',11))
# print(instance.method())
print(dir(instance))


ishas = hasattr(instance,'method')
print(ishas)