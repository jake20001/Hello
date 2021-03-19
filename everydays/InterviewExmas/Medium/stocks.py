# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/9/29 11:19
# FileName : stocks
# Description : 
# --------------------------------

# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

def max_profit(prices):
    bx = []
    for i in range(len(prices)-1):
        max_p = max(0, prices[i+1]-prices[i])
        bx.append(max_p)
    bx.sort()
    return bx

def max_profitk(prices,k):
    bx = max_profit(prices)
    return (bx[-1:-k-1:-1])




# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


if __name__ == '__main__':
    # prices = [7,1,5,3,6,4]
    prices = [3,3,5,0,0,3,1,4]
    prices = [3,2,6,5,0,3]
    k = 2
    # print(max_profit(prices))
    print(max_profitk(prices,k))
