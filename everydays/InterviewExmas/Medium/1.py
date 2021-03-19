# -*- coding:utf-8 -*-
# ----------------------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/4/27 11:29
# FileName : 1
# Description : 1,yield
#               2,hanoi
#               3,不重复的组合 combine
#                 备注：2,3两题在数学上有一致性
#               4,从数组中找出指定2数之和
#               5,找出指定数组最大值组合
#               6,Decorator
#               7,Sn = 1 + a + a^2 + ...... + a^n
# -----------------------------------------------

# ===========  yield  BEGIN ==============
def func(n):
    print("starting...")
    while True:
        res = yield n
        print("res:",res)

def yieldTest():
    g = func(1)
    print(next(g))
    # print("*"*20)
    # print(next(g))
    # print(g.send(7))
# =========== yield END ==================

# ============= Hanoi BEGIN ==============
def hanoi(n,s,d,fz,count,ax):
    if n==0:
        print("="*20)
    else:
        hanoi(n-1,s,fz,d,count,ax)
        print("move ",s," -> ",d)
        print('count => ',count)
        count += 1
        ax.append(1)
        hanoi(n-1,fz,d,s,count,ax)
    return ax
# ============= Hanoi END ================

# ============= Combine BEGIN ============
def combine(data):
    count = 0
    l = len(data)
    flag = []
    for i in range(l):
        flag.append(0)

    while True:
        for i in range(l):
            if flag[i] == 0:
                flag[i] = 1
                continue
            else:
                flag[i] = 0
                break
        for i in range(l):
            if flag[i]==1:
                print(data[i],end=' ')
        print()
        if 1 not in flag:
            break
        count = count+1
    return count

def subsets(nums):
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res

def subsets2(nums,n):
    ax = subsets(nums)
    bx = []
    for x in ax:
        if len(x)==n:
            bx.append(x)
    return bx
# ============= Combine END ================

# =========== find sum in array BEGIN ======
def hasSum(ax,target):
    bx = sorted(ax)
    l = len(bx)
    i = 0
    j = l-1
    while True:
        if bx[i]+bx[j]==target:
            print("i = ",i," j = ",j)
            return True
        elif bx[i]+bx[j]<target:
            i = i+1
        else:
            j = j-1
        if i>j:
            break
    return False
# =============== END ======================

# ========= 找出最大值k个数值 不能排序 BEGIN ==
def findMaxArr(ax,k):
    l = len(ax)
    assert k<l
    bx = []
    for i in range(k):
        bx.append(ax[i])
    for i in range(k,l):
        # 插入ax[i]到bx中
            b = min(bx)
            if b<ax[i]:
                bx.remove(b)
                bx.append(ax[i])
    return bx
# ================= END ===================

# ================= Decorator =============
def using_logger(func):

    def wrapper(*args,**kwargs):
        print(u"%s 装饰器 ..." % func.__name__)
        return func(*args)
    return wrapper

@using_logger
def bar():
    print("i am bar")
    return "OK"
# ================= END ===================

# ============= 级数：等比数列 =============
def Geometric(n,q):
    s = 0
    for i in range(n):
        x = 1
        for k in range(i):
            x = q*x
        s = s + x
    return s
# ============== END ======================

def main():
    # yieldTest()
    print("一共移动次数：",len(hanoi(3,'S','D','FZ',0,[])))
    # print("一共组合次数：",subsets([1,2,3,4,5]))
    # print("一共组合次数：",subsets2([1,2,3],2))
    # print("一共组合次数：",combine([1,2,3,4,5]))
    # # hasSum([1,5,7,3,9,8,6,3],10)
    # # print(findMaxArr([1,5,7,3,9,8,6,3],4))
    # # print(bar())
    # # print(Geometric(100,0.2))

if __name__ == '__main__':
    main()