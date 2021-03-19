# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/3 18:28
# FileName : day4.2
# Description : 
# --------------------------------

class Mama(object):
    def says(self):
        print("do your homework")

class Sister(Mama):
    def says(self):
        # Mama.says(self)
        super(Sister,self).says()
        print('and clean your bedroom')

anita = Sister()
anita.says()