# coding: utf-8
"""
    @author: zhangjk
    @file: 16.py
    @date: 2020-03-03
    说明：xxxx
"""


def f1(n):
    if n==1:
        return 1
    return n*f1(n-1)

# print(f1(5))


def f2():
    fd = open('name.txt','w')
    for i in range(1000):
        if i%2==0:
            txt = "张芮通\t"*10
        else:
            txt = "张芮智\t"*10
        print(txt)
        fd.write(txt+'\n')
    fd.close()


def pre_date(pre):
    def date(func):
        def wrapper():
            func(pre)
        return wrapper
    return date

# 加法口诀
@pre_date(1)
def f3(x):
    print('\033[0;36m' + str(x) + " 张芮通-加法口诀" + '\033[0m')
    for i in range(1,10):
        for j in range(1,i+1):
            if i%2==0:
                print('\033[0;36m' + str(j) + ' + ' + str(i-j+1) + ' = ' + str(i+1),end='\t' + '\033[0m')
            else:
                print(str(j) + ' + ' + str(i-j+1) + ' = ' + str(i+1),end='\t')
        print()

# 减法口诀
@pre_date(2)
def f4(x):
    print('\033[0;34m' + str(x) + " 张芮智-减法口诀" + '\033[0m')
    for i in range(1,10):
        for j in range(1,i+1):
            if i%2==0:
                print('\033[0;34m' + str(j) + " = " + str(i+1) + ' - ' + str(i-j+1),end='\t' + '\033[0m')
            else:
                print(str(j) + " = " + str(i+1) + ' - ' + str(i-j+1),end='\t')
        print()

# 乘法口诀
@pre_date(3)
def f5(x):
    print('\033[0;36m' + str(x) + " 张芮通-乘法口诀" + '\033[0m')
    for i in range(1,10):
        for j in range(1,i+1):
            if i%2==0:
                print('\033[0;36m' + str(j) + " * " + str(i) + ' = ' + str(j*i),end='\t' + '\033[0m')
            else:
                print(str(j) + " * " + str(i) + ' = ' + str(j*i),end='\t')
        print()

# 除法口诀
@pre_date(4)
def f6(x):
    print('\033[0;34m' + str(x) + " 张芮智-除法口诀" + '\033[0m')
    for i in range(1,10):
        for j in range(1,i+1):
            if i%2==0:
                print('\033[0;34m' + str(j) + " = " + zhengqi(j*i) + '/' + str(i) + '\033[0m',end='\t')
            else:
                print(str(j) + " = " + zhengqi(j*i) + '/' + str(i),end='\t')
        print()

def zhengqi(x):
    y = str(x)
    if len(y)==1:
        y = ' ' + y
    return y


# f2()
f3()
print('\033[0;31m' + '='*105 + '\033[0m')
f4()
print('\033[0;31m' + '='*105 + '\033[0m')
f5()
print('\033[0;31m' + '='*105 + '\033[0m')
f6()