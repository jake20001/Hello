# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 11:26
# FileName : 001
# Description : 
# --------------------------------

class A(object):

    def __init__(self,is_done):
        self.is_done = is_done

class B(A):

    def __init__(self,is_done):
        A.__init__(self,is_done)

a = A(False)
b = B(False)
a.is_done = True
print(a.is_done)
print(b.is_done)