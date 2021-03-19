# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/4 19:16
# FileName : day6.3
# Description : 
# --------------------------------

def enhancer_1(klass):
    c = [l for l in klass.__name__ if l.isupper()]
    klass.contracted_name = ''.join(c)
    print('output',klass.contracted_name)

def enhancer_2(klass):
    def logger(function):
        def wrap(*args,**kwargs):
            print('I log everything')
            return function(*args,**kwargs)
        return wrap
    for el in dir(klass):
        if el.startswith('_'):
            continue
        value = getattr(klass,el)
        print("xxxx",value)
        # print(dir(value))
        if not hasattr(value,'__class__'):
            continue
        print("111")
        setattr(klass,el,logger(value))

def enhance(klass,*enhancers):
    for enhancer in enhancers:
        enhancer(klass)

class MySimpleClass(object):
    def ok(self):
        return 'I lied'


enhance(MySimpleClass,enhancer_1,enhancer_2)
thats = MySimpleClass()
print(thats.contracted_name)
print(thats.ok())
# print(thats.contracted_name)

