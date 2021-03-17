# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/5 11:25
# FileName : mainfunc
# Description : 
# --------------------------------
import os
import sys

# from everydays.others.envtest.pathenv.beijingenv import Beijing
from everydays.others.envtest.pathenv.factory import Factory
# from everydays.others.envtest.pathenv.shenzhouenv import Shenzhen

current_dir = os.path.abspath(os.path.join(os.getcwd(), "pathenv"))
sys.path.append(current_dir)
print('beijing111111111',current_dir)

print()

from beijingenv import Beijing
from shenzhenenv import Shenzhen

factory = Factory()

beijing = Beijing()
beijing_case = factory.create(beijing)
shenzhen = Shenzhen()
shenzhen_case = factory.create(shenzhen)

beijing_case.call_func()
shenzhen_case.call_func()

