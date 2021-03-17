# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/4 19:04
# FileName : day1_env
# Description : 
# --------------------------------
import os
import sys

script_dir = os.path.abspath(os.path.join(os.getcwd(), "beijing"))
# script_dir = os.path.join(current_dir, "beijing")
# sys.path.append(script_dir)
print('beijing',script_dir)
# os.environ["PATH"] += script_dir


# os.getenv
# print("evn beijingenv",os.environ)
from beijing.beijingpath import get_path

class Beijing(object):

    def call_func(self):
        get_path()


# call_func()