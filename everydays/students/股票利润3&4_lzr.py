#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/12 15:29

from typing import List
import time

"""
思路，最终收益 = 卖出价格 - 总成本
    总成本 = 本次成本 - 之前收益
"""


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        buy_p1, buy_p2 = float('inf'), float('inf')
        max_p1, max_p2 = 0, 0
        for i in prices:
            buy_p1 = min(i, buy_p1)
            max_p1 = max(max_p1, i-buy_p1)
            buy_p2 = min(buy_p2, i-max_p1)
            max_p2 = max(max_p2, i-buy_p2)

        return max_p2


s = Solution3()
a = s.maxProfit([8,3,6,2,8,8,8,4,2,0,7,2,9,4,9])
print(a)


class Solution4:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) == 0:
            return 0
        if k>len(prices):
            k = len(prices)
        max_p = [0] * k
        buy_p = [float('inf')] * k
        for i in prices:
            buy_p[0] = min(buy_p[0], i)
            max_p[0] = max(max_p[0], i-buy_p[0])
            for j in range(1, k):
                buy_p[j] = min(buy_p[j], i-max_p[j-1])
                max_p[j] = max(max_p[j], i - buy_p[j])
        return max_p[-1]


s =Solution4()
a = s.maxProfit(2, [8,3,6,2,8,8,8,4,2,0,7,2,9,4,9])
print(a)