# coding: utf-8
"""
    @author: zhangjk
    @file: 14.py
    @date: 2020-03-01
    说明：xxxx
"""

class Foo(object):
    def __init__(self, height, weigth):
        self.height = height
        self.weigth = weigth

    @property
    def ratio(self):
        return self.height / self.weigth

    @property
    def pos_rel2abs(self):
        def convert(x, y):
            return x, y
        return convert

    @property
    def pos_rel2abs2(self):
        def convert(*args):
            return args
        return convert

foo = Foo(176, 120)
# print(foo.ratio)    # => 1.4666666666666666
print(foo.pos_rel2abs(1,2))
# print(foo.height)
# print(foo.pos_rel2abs2(2,3,5,6))
# print(foo.pos_rel2abs)