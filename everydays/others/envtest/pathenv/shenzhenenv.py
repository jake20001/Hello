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

# from everydays.others.envtest.shenzhen.shenzhoupath import get_path


script_dir = os.path.abspath(os.path.join(os.getcwd(), "shenzhen"))
# script_dir = os.path.join(current_dir, "shenzhen")
# sys.path.append(script_dir)
print('shenzhen',script_dir)

from shenzhen.shenzhenpath import get_path

class Shenzhen(object):

    def call_func(self):
        get_path()


# call_func()