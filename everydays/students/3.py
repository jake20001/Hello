# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/8/17 9:48
# FileName : 3
# Description : 
# --------------------------------
import copy


def fmax2(a):
    m = 0
    for i in range(1,len(a)+1):
        for j in range(0,len(a)-i+1):
            # s = 0
            # for k in range(j,j+i):
            #     s += a[k]
            s = sum(a[j:j+i])
            if s>m:
                m = s
                index = [j,j+i-1]
    return index,m

def fmax3(a):
    m = 0
    s = 0
    for i in range(len(a)):
        m = max(m,a[i])
        s = s + a[i]
        m = max(m,s)
    return m

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


def maxSubArrry2(ax):
    max_pre = -float('inf')
    max_cur = -float('inf')
    for i in ax:
        max_pre = max(max_pre,max_cur)
        max_cur = max(i,max_cur+i)
    return max_cur


def maxsum1(nums):
    max_pre = -float('inf')
    max_cur = -float('inf')
    for i in nums:
        max_cur = max(max_cur + i, i)
        max_pre = max(max_pre, max_cur)

    return max_pre




def maxSubArray(nums):
    for i in range(1,len(nums)):
        nums[i] += max(nums[i-1],0)
        # print(nums)
    return max(nums)


def loopArray2(nums,value):
    for i in range(len(nums)):
        s = 0
        for j in range(i,len(nums)):
            s = s + nums[j]
            if s==value:
                return nums[i:j+1]
    return False

def loopArray(a,n):
    b = []
    for i in range(n,0,-1):
        n-=a[i]
        # print(a[i],end=' ')
        b.append(a[i])
        if(n==0):
            break
    b.reverse()
    return b


def main():
    ax = [-10,-3,-1,-6,1,-2]
    # index, m = fmax2(ax)
    # print(index[0],index[1],m)
    # bx = copy.deepcopy(ax)
    # value = maxSubArray(ax)
    # print(value)
    # n = ax.index(value)
    # # print(loopArray(bx,value))
    # print(loopArray(bx,n))
    # print(maxSubArrry2(ax))
    print(maxsum1(ax))
    # print(MaxConValue(ax))
    # print(fmax3(ax))
    # print(maxSubArray(ax))


if __name__ == '__main__':
    main()