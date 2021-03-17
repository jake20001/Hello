# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : apps
# Author : zhangjk
# CreateTime : 2021/3/17 10:25
# FileName : main_initial
# Description : 
# --------------------------------

from ViechleApp.apps.app_factory import AppFactory

name = 'A01'
app = AppFactory(name).create_app()
print(app.name)
app.download()
app.upgrade()

