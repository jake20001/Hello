# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/17 20:51
# FileName : day10.1
# Description : 工厂
# --------------------------------

def mtype():
    MyType = type('MyType',(object,),{'a':1})
    ob = MyType()
    print(ob)
    print(ob.a)
    print(isinstance(ob,object))

# equals
class MyType(object):

    a = 1

ob = MyType()
print(ob.a)
