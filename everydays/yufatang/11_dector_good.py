# coding: utf-8
"""
    @author: zhangjk
    @file: 10_dector_good.py
    @date: 2020-02-28
    说明：xxxx
"""

from datetime import datetime
# Create your tests here.
class params:
    def __init__(self):
        print("init called")

    def __setattr__(self, key, value):
        return super.__setattr__(key, value)

    @staticmethod
    def released():
        print("release this class")


def pre_date(cls,name):
    cls.name = name
    def date(func):
        def wrapper():
            print("before %s ,we called (%s)." % (func.__name__,cls))
            try:
                func()
                date = datetime.utcnow()
                print (date)
                print(cls.name)
            finally:
                cls.released()
        return wrapper
    return date

@pre_date(params,'Alan')
def alan():
    print ('alan speaking')

@pre_date(params,'Tom')
def tom():
    print ('tom speaking')

alan()