# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/5/21 10:29
# FileName : 1
# Description : 
# --------------------------------

def f1():
    return sum(range(1,101))

def f2():
    dic = {"name":'hz',"age":1}
    # del dic['name']
    dic.pop('name')
    print(dic)
    dic2 = {"name":'nan'}
    dic.update(dic2)
    print(dic)

def f3():
    with open('xx.txt','w') as f:
        f.write("aaa")

def f4():
    lis = [1,2,3,4,5]

    def fn(x):
        return x**2

    res = map(fn,lis)
    rest = [i for i in res if i>10]
    return rest

def f5():
    import random
    import numpy as np
    result = random.randint(10,20)
    res = np.random.rand(5)
    ret = random.random()
    print("正整数",result)
    print("5个随机小数",res)
    print("随机小数",ret)

def f6():
    import re
    nstr = '<div class="nam">中国</div>'
    res = re.findall(r'<div class=".*">(.*)</div>',nstr)
    print(res)

def f7():
    a = 2
    b = 2
    print(id(a),' --> ',id(b))
    c = [1,2]
    d = [1,2]
    print(id(c),' --> ',id(d))


def f8():
    nstr = 'ajdjdahwndpdal'
    nstr = set(nstr)
    nstr = list(nstr)
    nstr.sort()
    nstr = "".join(nstr)
    print(nstr)


def pre_date(a,b):
    def date(func):
        def wrapper():
            return func(a,b)
        return wrapper
    return date

def f9():
    mul = lambda a,b:a*b
    print(mul(4,5))

@pre_date(4,5)
def f10(*args):
    return args[0]*args[1]

@pre_date(4,5)
def f11(a,b):
    return a*b


def f12():
    dic = {"name":'zs',"age":18,"city":"深圳","tel":"12232424"}
    lis = sorted(dic.items(),key=lambda i:i[0])
    print(lis)
    dic = dict(lis)
    print(dic)


def f13():
    from collections import Counter
    a = 'jdawudnanduw;uwafandg.'
    res = Counter(a)
    print(res)
    b = {'a':1,'b':1,'C':2}
    resb = Counter(b)
    print(resb)
    c = ['ad','ac','ad','ar','cc','dd']
    resc = Counter(c)
    print(resc)


def f13_1():
    from collections import Counter
    a = 'jdawudnanduw;uwafandg.'
    res = Counter(a)
    print(res)
    b = list(a)
    c = dict()
    d = set()
    # 扫描
    for i in b:
        d.add(i)
    print(d)
    for i in d:
        c[i]=0
    for i in b:
        c[i] = c[i]+1
    print(c)


def f14():
    import re
    a = "not 404 found 张三 99xy 深圳"
    lis = a.split()
    print(lis)
    # xx = '([1-9]\d*.\d*|0.\d*[1-9]\d*) (.*$)'
    x = '\d*[a-zA-Z]+|\d+|[a-zA-Z]+'
    res = re.findall(x,a)
    for i in res:
        if i in lis:
            lis.remove(i)
    new_str = ' '.join(lis)
    print(res)
    print(lis)
    print(new_str)


def f15():
    a = [1,2,3,4,5,6,7,8,9,10]
    def fn(a):
        return a%2==1
    newlist = filter(fn,a)
    print(list(newlist))


class A(object):
    def __init__(self):
        print("init",self)
        print("self",id(self))

    def __new__(cls, *args, **kwargs):
        print("cls ID",id(cls))
        print("new",object.__new__(cls))
        return object.__new__(cls)



def main():
    # print(f1())
    # f2()
    # a = A()
    # print("a",id(A))
    # print("self a",id(a))
    # print(f4())
    # f5()
    # f6()
    # f7()
    # f8()
    # f9()
    # print(f11())
    # f12()
    # f13()
    # f13_1()
    # f14()
    f15()


if __name__ == '__main__':
    main()

