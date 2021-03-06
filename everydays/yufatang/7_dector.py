# coding: utf-8
"""
    @author: zhangjk
    @file: 6_dector.py
    @date: 2020-02-28
    说明：xxxx
"""

# 用于模拟对象的装饰器--类装饰器

def outer(clss):         # 类装饰器
    class Inner(object):
        def __init__(self):
            self.clss = clss()

        def __getattr__(self, attr):
            return getattr(self.clss, attr)

        def __setattr__(self, key, value):
            return super().__setattr__(key, value)

    return Inner


@outer          # Zoo = outer(Zoo)
class Zoo(object):
    def __init__(self):
        pass

    def say(self,name):
        print(name + ' hello world!')

zoo = Zoo()
zoo.name = 'Huahua'
print(zoo.__class__)    # <class '__main__.outer.<locals>.Inner'>
zoo.say(zoo.name)               # hello world!
