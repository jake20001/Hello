# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : apps
# Author : zhangjk
# CreateTime : 2021/3/17 10:26
# FileName : app_factory
# Description : 
# --------------------------------
from ViechleApp.apps.A01.initial import A01
from ViechleApp.apps.A02.initial import A02

projects = {"A01":A01(),"A02":A02()}

class AppFactory(object):

    def __init__(self,name):
        self.name = name

    def create_app(self):
        app = projects[self.name]
        app.name = self.name
        return app

    def register_app_hook(self, func):
        self.func = func