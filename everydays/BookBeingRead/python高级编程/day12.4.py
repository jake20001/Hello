# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/18 15:23
# FileName : day12.4
# Description : 
# --------------------------------

class Vlist(list):
    def accept(self,visitor):
        visitor.visit_list(self)

class Vdict(dict):
    def accept(self,visitor):
        visitor.visit_dict(self)

# ===============================
class Printer(object):
    def visit_list(self,ob):
        print(ob)

    def visit_dict(self,ob):
        print(ob)

def visit(visited,visitor):
    cls = visited.__class__.__name__
    meth = 'visit_%s'%cls
    method = getattr(visitor,meth,None)
    # print(method)
    if method:
        method(visited)

# a_list = Vlist([1,2,3])
# a_list.accept(Printer())
#
# a_dict = Vdict({'one':1,'two':2})
# a_dict.accept(Printer())

visit([1,2,3],Printer())

visit({'one':1,'two':2},Printer())