# coding: utf-8
"""
    @author: zhangjk
    @file: 12_dector.py
    @date: 2020-02-28
    说明：xxxx
"""

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()

