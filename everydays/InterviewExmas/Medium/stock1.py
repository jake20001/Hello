# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/9/22 19:27
# FileName : stock1
# Description : 
# --------------------------------

class Stock(object):

    def __init__(self):
        pass

    def get_max_value(self,ax):
        min_value = float('inf')
        max_value = -float('inf')
        bx = [0,0]
        for i in range(len(ax)):
            # min_value = min(ax[i],min_value)
            if ax[i]<min_value:
                min_value = ax[i]
                bx[0] = i
            # max_value = max(ax[i]-min_value,max_value)
            if ax[i]-min_value>max_value:
                max_value = ax[i]-min_value
                bx[1] = i
        return max_value,bx


def main():
    mStock = Stock()
    print(mStock.get_max_value([2,3,1,5,6]))


if __name__ == '__main__':
    main()
