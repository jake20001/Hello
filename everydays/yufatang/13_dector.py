# coding: utf-8
"""
    @author: zhangjk
    @file: 13_dector.py
    @date: 2020-02-28
    说明：xxxx
"""

# class Foo(object):
#     def __init__(self, height, weigth):
#         self.height = height
#         self.weigth = weigth
#
#     @property
#     def ratio(self):
#         return self.height / self.weigth
#
# foo = Foo(176, 120)
# print(foo.ratio)    # => 1.4666666666666666



class Prop(object):
    def __init__(self, fget):
        self.fget = fget

    def __get__(self,args, kwargs):
        return self.fget(args)

class Foo(object):
    def __init__(self, height, weigth):
        self.height = height
        self.weigth = weigth

    @Prop
    def ratio(self):
        return self.height / self.weigth

foo = Foo(176, 120)
print(foo.ratio)    # => 1.4666666666666666