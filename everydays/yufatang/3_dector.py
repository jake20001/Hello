# coding: utf-8
"""
    @author: zhangjk
    @file: 3_dector.py
    @date: 2020-02-28
    说明：xxxx
"""

def warp(obj):
    obj.name = 'python'
    return obj

@warp       # => foo = warp(foo)
def foo():
    pass

print(foo.name)         # => python

# @warp        # => Bar = warp(Bar)
# class Bar(object):
#     def __init__(self):
#         pass
#
# print(Bar.name)     # => python
