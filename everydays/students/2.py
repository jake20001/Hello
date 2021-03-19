# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/8/15 18:05
# FileName : 2
# Description : 
# --------------------------------

def fmax(a):
    imax = a[0] + a[1]
    index = 0
    for i in range(1,len(a)-1):
        if (a[i]+a[i+1])>imax:
            imax = a[i] + a[i+1]
            index = i
    return index

def maxArray2(nums):
    for i in range(1,len(nums)):
        nums[i-1] += nums[i]
    return max(nums[:-1])

import copy


def maxArray(nums) -> int:
    for i in range(1, len(nums)):
        nums[i - 1] += nums[i]
    #    nums.pop()
    #     print(nums)
    print(max(nums[:-1]))
    # list.index()
    print(nums.index(max(nums[:-1])))
    return nums.index(max(nums[:-1]))



def main():
    ax = [2,2,-2,3,4,1]
    # print(fmax(a))
    print(maxArray(ax))
    b = [-2, 1, -3, 5, -1, 2, 1, -5, 4]
    print(maxArray2(b))
    # print(id(b))
    # a = copy.deepcopy(b)
    # print(id(a))
    # m = maxArray(b)
    # print(a[m], a[m + 1])



if __name__ == '__main__':
    main()