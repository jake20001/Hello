# -*- coding: utf-8 -*-
# ////////////////////////////////////////////////////////////////失败的版本数组变长以后结果就不对
# class Solution(object):
#     def __init__(self):
#         pass
#
#     def maxProfit(self, prices):
#         p = 0
#         q = len(prices) - 1
#         flag = 0
#         if not prices:
#             return 0
#         _min = prices[p]
#         _max = prices[q]
#         res=0
#         while q > p:
#             if flag == 0:
#                 if prices[p + 1]<_min:
#                     flag = 1
#                 else:
#                     if prices[p+1]>_max:
#                         res=max((prices[p+1]-prices[p]),res)
#                 _min = min(_min, prices[p+1])
#                 p += 1
#             elif flag == 1:
#                 if prices[q - 1]>_max:
#                     flag = 0
#                 else:
#                     if prices[q-1]<_min:
#                         res=max((prices[q]-prices[q-1]),res)
#                 _max = max(_max, prices[q-1])
#                 q -= 1
#         if _max - _min < 0:
#             return 0
#
#         return max((_max - _min),res)
#
# a = Solution()
# print(a.maxProfit([1,4,2]))
# print(a.maxProfit([3,2,6,5,0,3]))
# print(a.maxProfit([3,3,5,0,0,3,1,4]))
# print(a.maxProfit([1,2,4,2,5,7,2,4,9,0,9]))
# print(a.maxProfit([5,2,5,6,8,2,3,0,1,8,5,2,1]))

# ////////////////////////////////////////////////////////////////// 重新思考以后的版本
class Solution(object):
    def __init__(self):
        pass

    def maxProfit(self, prices):
        p = 0
        q = 1
        t = []
        while q < len(prices):
            if (prices[p] >= prices[q]):
                p = q
                q += 1
            else:
                t.append(prices[q] - prices[p])
                q += 1

        return max(t) if t else 0


a = Solution()
print(a.maxProfit([1, 4, 2]))
print(a.maxProfit([3, 2, 6, 5, 0, 3]))
print(a.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(a.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))
print(a.maxProfit([5, 2, 5, 6, 8, 2, 3, 0, 1, 8, 5, 2, 1]))
print(a.maxProfit([2,1]))
