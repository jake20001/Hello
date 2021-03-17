# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/5 10:49
# FileName : mainstart
# Description : 
# --------------------------------
from everydays.others.factorytest.factory1 import ToysFactory
from everydays.others.factorytest.lion import Lion
from everydays.others.factorytest.tiger import Tiger

factory = ToysFactory()

def command1():
    tiger_case = Tiger('mao')
    case = factory.create_toy(tiger_case)
    case.run()

def command2():
    lion_case = Lion('lion')
    case = factory.create_toy(lion_case)
    case.run()

mt = {1:command1,2:command2}

mt[2]()