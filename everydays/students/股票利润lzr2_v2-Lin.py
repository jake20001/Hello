#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/27 19:03


def max_profit2(prices):
    max_p = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_p += (prices[i] - prices[i-1])
    return max_p


if __name__ == '__main__':
    prices = [5,4,3,1,5,4,8]
    print(max_profit2(prices))