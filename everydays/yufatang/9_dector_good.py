# coding: utf-8
"""
    @author: zhangjk
    @file: 9_dector_good.py
    @date: 2020-02-28
    说明：xxxx
"""
from datetime import datetime


def pre_date(pre):
    def date(func):
        def wrapper():
            func()
            date = datetime.utcnow()
            print(pre + str(date))
        return wrapper
    return date

@pre_date('Today is :')
def alan():
    print ('alan speaking')

@pre_date('I am Tom :')
def tom():
    print ('tom speaking')

alan()


