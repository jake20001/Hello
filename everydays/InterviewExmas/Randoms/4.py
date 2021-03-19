# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/5/21 18:44
# FileName : 4
# Description : 
# --------------------------------


def f1():
    A = zip(('a','b','c'),(1,2,3))
    print(A)
    di = [i for i in A]
    print(di)
    d = dict(A)
    print(d)


def f2(key,value,dic={}):
    dic[key] = value
    print(dic)

def fn():
    f2('one',1)
    f2('two',2)
    f2('three',3,{})

def f3():
    bx = ['',[],{},(),None,False,0]
    ax = [1,-1]
    for i in range(len(bx)):
        ax.append(bx[i])
        print(any(ax))
        print(all(ax))
        print(ax)
        ax.pop()

def f4():
    import copy
    a = "hello World!"
    b = a
    print(id(a))
    print(id(b))
    c = copy.copy(a)
    print(id(c))
    d = copy.deepcopy(a)
    print(id(d))
    ax = ["Hello World","Hello Java",['aa','bb']]
    bx = ax
    print('ax',id(ax))
    print('bx',id(bx))
    cx = copy.copy(ax)
    print('cx',id(cx))
    dx = copy.deepcopy(ax)
    print('dx',id(dx))
    ax[0] = "KKKK"
    print('ax0',id(ax),ax)
    print('bx0',id(bx),bx)
    print('cx0',id(cx),cx)
    print('dx0',id(dx),dx)
    ax[2][0] = "KKKK"
    print('ax1',id(ax),ax)
    print('bx1',id(bx),bx)
    print('cx1',id(cx),cx)
    print('dx1',id(dx),dx)


def f5():
    a = [i for i in range(3)]
    print(a)
    b = (i for i in range(3))
    print(b)
    print(list(b))


def f6():
    foo = [-5,8,0,4,9,20]
    a = sorted(foo,key=lambda x:x)
    print(a)
    foo.sort(key=lambda x:x,reverse=True)
    print(foo)

def f7():
    foo = [-5,-2,-4,8,0,4,9,20]
    a = sorted(foo,key=lambda x:(x<0, abs(x)))
    print(a)

def f7_1():
    foo = [-5,-2,-4,8,0,4,9,20]
    ax = []
    for i in foo:
        if i>=0:
            ax.append(i)
    for i in range(len(ax)):
        foo.remove(ax[i])
    print(ax)
    print(foo)
    ax.sort()
    foo.sort(reverse=True)
    ax.extend(foo)
    print(ax)

def f8():
    dic = [{'name':'zs','age':19},{'name':'ll','age':24},{'name':'wa','age':17},{'name':'df','age':29}]
    a = sorted(dic,key=lambda x:x.keys())
    print(a)
    # c = sorted(dic,key=lambda x:x.values())
    # print(c)
    b = sorted(dic,key=lambda x:x['name'])
    print(b)

def f9():
    dic = [('zs',19),('ll',24),('wa',17),('df',29)]
    a = sorted(dic,key=lambda x:x[0])
    print(a)
    b = sorted(dic,key=lambda x:x[1])
    print(b)

def f10():
    dic = [['zs',19],['ll',24],['wa',17],['df',29],['df',10]]
    a = sorted(dic,key=lambda x:(x[0],x[1]))
    print(a)
    b = sorted(dic,key=lambda x:x[1])
    print(b)

def f11():
    dic = {'name':'zs','sex':'man','city':'bj'}
    # foo = zip(dic.keys(),dic.values())
    foo = dic.items()
    print(foo)
    # l = list(foo)
    # print(l)
    l = foo
    a = sorted(l,key=lambda x:x[0])
    print(a)
    new_dic = {x[0]:x[1] for x in a}
    print(new_dic)


def main():
    # f1()
    # fn()
    # f3()
    # f4()
    # f5()
    # f6()
    # f7()
    # f7_1()
    # f8()
    # f9()
    # f10()
    f11()

if __name__ == '__main__':
    main()