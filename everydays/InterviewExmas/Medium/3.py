# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/5/18 15:16
# FileName : 3
# Description : 求数组中连续值的和最大值的组合
# --------------------------------

def MaxConValue(ax):
    l = len(ax)
    s1 = ax[0]
    for i in range(l):
        s2 = ax[i]
        if s2 > s1:
            s1 = s2
        for j in range(i+1,l):
            s2 = s2 + ax[j]
            if s2 > s1:
                s1 = s2
    return s1


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
    # -1,2,4,-3,1,8
    # [-1,2,-1]
    ax = [3,-8,0,1]
    # ax = [3,-8,0,1,1,1,1,1,3,-8,0,1,1,1,1,1,3-8,0,1,1,1,1,1,3-8,0,1,1,1,1,1,3,1]
    # print(MaxConValue(ax))
    print(maxsum1(ax))
    # max_pre,x = maxsum(ax)
    # print(getAx(max_pre,x,ax))



if __name__ == '__main__':
    main()
