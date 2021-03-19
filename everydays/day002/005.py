# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 14:19
# FileName : 005
# Description : 
# --------------------------------

class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, attrs):
        uppercase_attr = {}
        for name, val in attrs.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

    def __call__(cls):
        return super(UpperAttrMetaclass, cls).__call__()

m = UpperAttrMetaclass('UpperAttrMetaclass',(object,),{'aaa':'aaa'})
print(m.__dict__)
print(m())
print(m().__dict__)
