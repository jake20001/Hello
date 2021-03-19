# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/5/22 13:47
# FileName : 6
# Description : 
# --------------------------------

class Animal(object):

    def __init__(self,name):
        self.name = name
        print('__init__',self.name)

    def __del__(self):
        print("__del__ Method")

    def visit(self):
        print(id(self))

class List(object):

    def __init__(self,lst):
        self.lst = lst

    def visit(self):
        print(self)

    def __del__(self):
        print(self,'__del__')

def f2():
    import gc
    mList = List([i for i in range(10)])
    mList1 = mList
    mList.lst[1] = 20
    print(list(mList.lst),mList,id(mList.lst))
    print(list(mList1.lst),mList1,id(mList1.lst))
    print(gc.collect())
    a = mList.lst[0]
    del mList.lst
    print(gc.collect())
    print(a)
    # print(list(mList.lst),mList)
    print(mList1)
    # 非常好，证明了地址的唯一性  ，Good
    print(list(mList1.lst),mList1)


def f1():
    import time
    cat = Animal("CAT")
    cat2 = cat
    cat3 = cat
    print(id(cat))
    # GOOD , 证明了地址的唯一性
    del cat.name
    print(id(cat2.name))
    # END
    print(id(cat3))
    # print(id(cat))
    # time.sleep(2)
    print(id(cat2))
    print(id(cat3))
    cat2.visit()


def f3():
    import re
    title = '你好,hello,世界,kkk,二货'
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    print(pattern)
    result = pattern.findall(title)
    print(result)

    pattern2 = r'[\u4e00-\u9fa5]+'
    res = re.findall(pattern2,title)
    print(res)

    pattern3 = r'([\u4e00-\u9fa5]+),hello,([\u4e00-\u9fa5]+)'
    ress = re.search(pattern3,title)
    print(ress)
    if ress:
        print(ress.group())
        print(ress.groups())
        print(ress.group(1))
        print(ress.group(2))

    res1 = re.match(pattern2,title)
    print(res1)
    if res1:
        print(res1.group())

    # res2 = re.fullmatch(pattern2,title)
    # print(res2)
    # if res2:
    #     print(res2.group())

def f4():
    import re
    labels = ['<html><h1>www.itest.com</h1></html>','<html><h1>www.itest.com</h2></html>']
    for label in labels:
        ret = re.match(r"<(\w*)><(\w*)>.*?</\2></\1>",label)
        if ret:
            print(ret.group())

def f5():
    a = ['苏州','中国','','','日本']
    res = map(lambda x:"填充值" if x=='' else x,a)
    res1 = ["填充值" if x=='' else x for x in a]
    print(list(res))
    print(res1)

def f6():
    import pandas as pd
    df = pd.read_excel('test1.xlsx')
    print(df)


def f7(ax):
    pre = -1
    pre_max = -1
    for i in ax:
        pre = max(pre+i,i)
        pre_max = max(pre,pre_max)
    return pre_max


def main():
    # f1()
    # f2()
    # f3()
    # f4()
    # f5()
    # f6()
    print(f7([-1,-1,2,-1,3]))



if __name__ == '__main__':
    main()