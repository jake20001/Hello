# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/5 10:44
# FileName : factory1
# Description : 
# --------------------------------

class ToysFactory(object):

    def create_toy(self,case):
        return case

    def run_case(self):
        print("-----")

