# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/5 10:47
# FileName : Tiger
# Description : 
# --------------------------------

class Tiger(object):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "Create " + self.name

    def run(self):
        print("%s 1111111111"%(self))