# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 13:39
# FileName : 003
# Description : 
# --------------------------------

class Funky(metaclass=type):

    def __init__(self):
        print("11111")
        return super().__init__()

    def __new__(cls, *args, **kwargs):
        print("22222")
        return super().__new__(cls)

    def __call__(self,*args, **kwargs):
        print("Look at me, I work like a function!")

    def __str__(self):
        return "33333"

f = Funky()
print(f)
