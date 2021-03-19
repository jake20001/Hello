# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/5/18 16:48
# FileName : 5
# Description : 
# --------------------------------

# from collections import Iterable
# from collections import Iterator


def f1(iterables):
    for it in iterables:
        yield it

def f2(*iterables):
    for it in iterables:
        yield it

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

def chain2(*iterables):
    for i in iterables:
        yield from i


def fiter():
    a = [1,2,3]
    print(list(a))
    b = (1,2,3)
    print(list(b))
    c = {'a':1,'b':2,'c':3}
    print(list(c))
    print(c.__getitem__('a'))
    print(list(c.keys()))
    d = '123'
    print(list(d))


# def flatten(items, ignore_types=(str, bytes)):
#     for x in items:
#         if isinstance(x, Iterator) and not isinstance(x, ignore_types):
#             yield from flatten(x)
#         else:
#             yield x
#
# def Mainflatten():
#     items = [1, 2, [3, 4, [5, 6], 7], 8]
#     for x in flatten(items):
#         print(x)
#
# def Mainflatten2():
#     items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
#     for x in flatten(items):
#         print(x)


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

    # 一般情况
    def VisitNodes(self,root):
        print('node',root)
        for node in root:
            self.VisitNodes(node)



def CreateNodes():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    # for ch in root.depth_first():
    #     print(ch)
    root.VisitNodes(root)

# class MyRoot(object):
#
#     def __init__(self,value):
#         self.value = value

# 二叉树
class MyNode(object):

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def AddLeftChild(self,node):
        self.left = node

    def AddRightChild(self,node):
        self.right = node

    def VisitNodes(self,root):
        # print('node',root.value,'->',root.left.value)
        # print('node',root.value,'->',root.right.value)
        if root.left!=None:
            print('node',root.value,'->',root.left.value)
            self.VisitNodes(root.left)
        if root.right!=None:
            print('node',root.value,'->',root.right.value)
            self.VisitNodes(root.right)
        print('node',root.value,'-> None')




def main():
    # s = 'ABC'
    # print(next(f2(s)))
    # print(list(f2(s)))
    # print(next(f1(s)))
    # print(list(f1(s)))
    # t = tuple(range(3))
    # print(list(chain(s, t)))
    # print(list(chain2(s, t)))
    # fiter()
    # Mainflatten()
    # CreateNodes()

    # 构建一个二叉树
    root = MyNode(0)
    child1l = MyNode(1)
    child1r = MyNode(2)
    root.AddLeftChild(child1l)
    root.AddRightChild(child1r)
    child1l2l = MyNode(3)
    child1l2r = MyNode(4)
    child1l.AddLeftChild(child1l2l)
    child1l.AddRightChild(child1l2r)
    child1r2l = MyNode(5)
    child1r.AddLeftChild(child1r2l)
    root.VisitNodes(root)


if __name__ == '__main__':
    main()