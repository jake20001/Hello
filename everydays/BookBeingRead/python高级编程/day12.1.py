# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/18 11:05
# FileName : day12.1
# Description : 
# --------------------------------
import os


class DublinCoreAdapter(object):
    def __init__(self,filename):
        self._filename = filename

    def title(self):
        return os.path.splitext(self._filename)[0]

    def creater(self):
        return "Someone"

    def language(self):
        return ('en',)


class DublinCoreInfo(object):
    def summary(self,dc_ob):
        print('Title %s'%dc_ob.title())
        print('Create %s'%dc_ob.creater())
        print('Languge %s'%','.join(dc_ob.language()))


adapter = DublinCoreAdapter('1.txt')
infos = DublinCoreInfo()
infos.summary(adapter)
