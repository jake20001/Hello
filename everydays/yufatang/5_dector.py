# coding: utf-8
"""
    @author: zhangjk
    @file: 5_dector.py
    @date: 2020-02-28
    说明：xxxx
"""

# 用于模拟对象的装饰器--类方法装饰器
def outer(obj):         # 类方法装饰器
    def inner(self):
        print('hello inner')
        obj(self)

    return inner

class Zoo(object):
    def __init__(self):
        pass

    @outer        # => zoo = outer(zoo)
    def zoo(self):
        print('hello zoo')

z = Zoo()
print(z.zoo.__name__)
z.zoo()
