# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/7/30 18:11
# FileName : 2
# Description : 
# --------------------------------

def findIndex2(ax,target):
    for i in range(len(ax)):
        for j in range(i,len(ax)):
            if target-ax[j]==ax[i]:
                return i,j
    return 0

def findIndex(ax,target):
    for i in range(len(ax)):
        if target-ax[i] in ax:
            return i
    return 0


def findArraysIndex(ax,target,idx):
    for i in range(idx+1,len(ax)):
        if ax[idx] + ax[i]==target:
            return idx,i
    return 0


def main():
    ax = [-1,8,-1,3,6,5]
    target = 14
    print(findIndex2(ax,target))
    print(findArraysIndex(ax,target,findIndex(ax,target)))


if __name__ == '__main__':
    main()