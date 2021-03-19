# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/8/3 19:32
# FileName : 8
# Description : 求数组中相邻两数之和最大的组
# --------------------------------


def MaxArray(ax):
    if len(ax)<2:
        return
    bx = (0,1)
    if len(ax)<3:
        return bx
    m1 = ax[0] + ax[1]
    for i in range(1,len(ax)-1):
        m2 = ax[i] + ax[i+1]
        if m2>=m1:
            m1 = m2
            bx = (i,i+1)
    return m1,bx


def main():
    ax = [2,2,-2,3,4,1]
    print(MaxArray(ax))


if __name__ == '__main__':
    main()

