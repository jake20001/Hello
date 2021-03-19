# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/7/30 18:53
# FileName : 4
# Description : 
# --------------------------------


def gys(a,b):
    if a < b:
        b,a = a,b
    while a%b!=0:
        a,b = b,a%b
    print(b)

def maxsum1(nums):
    max_pre = -float('inf')
    max_cur = -float('inf')
    for i in nums:
        max_cur = max(max_cur + i, i)
        max_pre = max(max_pre, max_cur)
    return max_pre


def getAx(max_pre,x,nums):
    s = 0
    isBegin = False
    ax = []
    for n in nums:
        if s==max_pre:
            break
        if n==x:
            isBegin = True
        if isBegin:
            s = s + n
            ax.append(n)
    return ax


def maxsum(nums):
    max_pre = -float('inf')
    print(max_pre)
    max_cur = -float('inf')
    x = max_cur
    for i in nums:
        if max_cur+i>i:
            max_cur = max_cur+i
        else:
            max_cur = i
            x = i
        if max_cur>max_pre:
            max_pre = max_cur
    return max_pre,x


def main():
    ax = [-1,1,-2,20,-1,4,-3,1]
    # print(MaxConValue(ax))
    # print(maxsum1(ax))
    max_pre,x = maxsum(ax)
    print(getAx(max_pre,x,ax))

if __name__ == '__main__':
    main()