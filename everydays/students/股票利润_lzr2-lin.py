#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/27 10:01

def max_profit(prices):
    max_p = 0
    for i in range(len(prices)-1):
        max_p += max(0, prices[i+1]-prices[i])
    return max_p


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(max_profit(prices))
