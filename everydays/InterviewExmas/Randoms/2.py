# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/5/21 15:50
# FileName : 2
# Description : 
# --------------------------------


def f1(a):
    res = [i for i in a if i%2==1]
    return res

def f2():
    ax = [1,5,7,9]
    bx = [2,2,6,8]
    ax.extend(bx)
    print(ax)
    ax.sort()
    print(ax)

def f2_1():
    ax = [1,5,7,9,9,11,18]
    bx = [2,3,6,8,10]
    cx = []
    if len(ax)<len(bx):
        # tmp = ax
        # ax = bx
        # bx = tmp
        ax,bx = bx,ax
    print(ax)
    print(bx)
    j = 0
    i = 0
    while i < len(ax):
        a = ax[i]
        b = bx[j]
        if b>a:
            cx.append(a)
            i += 1
        else:
            cx.append(b)
            if j==len(bx)-1:
                break
            else:
                j += 1
    print('i',i)
    for z in range(i,len(ax)):
        cx.append(ax[z])
    print(cx)
    return cx

def f3():
    import datetime
    riqi = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    week = datetime.datetime.now().isoweekday()
    print(riqi)
    print(week)

def f4():
    import pychart
    # pychart.pychart_util.info()

def f5():
    ax = [[1,2],[3,4],[5,6]]
    x = [j for i in ax for j in i]
    print(x)

def f5_1():
    ax = [[1,2],[3,4],[5,6]]
    x = [j for j in ax]
    bx = []
    for i in x:
        bx = bx + i
    return bx

def f6():
    x = 'abc'
    x = '->'
    y = list('def')
    print(y)
    z = ['d','e','f']
    m = x.join(y)
    n = x.join(z)
    print(m)
    print(n)

def f7():
    a = [1,2]
    b = [3,4]
    res = [i for i in zip(a,b)]
    print(res)

    a = (1,2)
    b = (3,4)
    res = [i for i in zip(a,b)]
    print(res)

    a = 'ab'
    b = 'xyz'
    res = [i for i in zip(a,b)]
    print(res)

def f8():
    import re
    a = "zhangsan 98score"
    ret = re.sub(r"\d+",'100',a)
    print(ret)

def f9():
    a = b"hello"
    b = "你好".encode()
    print(a,b)
    print(type(a),type(b))

def f10(ax,new_list):
    a = min(ax)
    ax.remove(a)
    new_list.append(a)
    if len(ax)>0:
        f10(ax,new_list)
    return new_list

def f10_1(ax):
    for i in range(len(ax)):
        for j in range(i+1,len(ax)):
            if ax[i]>ax[j]:
                ax[i],ax[j] = ax[j],ax[i]
    return ax


def main():
    # print(f1([1,2,3,4,5,6,7,8,9,10]))
    # f2()
    # f2_1()
    # f3()
    # f4()
    # f5()
    # print(f5_1())
    # f6()
    # f7()
    # f8()
    # f9()
    # print(f10([2,5,3,4,9,6],[]))
    print(f10_1([2,5,3,4,9,6]))



if __name__ == '__main__':
    main()
