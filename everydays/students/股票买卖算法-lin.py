#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/18 17:47
"""
题目：
    给定一个数组，它的第i个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    注意：你不能在买入股票前卖出股票。
思路：
    思路1：每天都买入股票，取往后到结束中股票价格最高值减去买入价格，求出当天买入的最高收益，
        在与前一天买入股票能获得的最高收益比较，取更大众值，最终求出收益的最大值。
    思路2：假设第一天买入价格最低，当天买入，从第二天开始卖出，比较哪天卖出收益更大；同时，遇到比买入价格更低的
    股票，则买入价格更低的股票，继续从第二天开始卖出，比较哪天卖出收益更大，最终值即为最大收益
"""


def solution(a):
    max_p = -float('inf')
    for i in range(len(a)-1):
        max_p = max(max(a[i+1: len(a)]) - a[i], max_p)
    if max_p < 0:
        return 0
    return max_p


def solution2(a):
    buy_in = float('inf')
    max_p = -float('inf')
    for i in range(len(a)-1):
        buy_in = min(a[i], buy_in)
        max_p = max(a[i+1]-buy_in, max_p)
    if max_p < 0:
        return 0
    return max_p


if __name__ == '__main__':
    a = [1, 2, 1, 4, 3, 4, 5, 6, 8, 0, 6, 4, 0]
    print(solution(a))
    print(solution2(a))
