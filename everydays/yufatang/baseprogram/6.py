# coding: utf-8
"""
    @author: zhangjk
    @file: 16.py
    @date: 2020-02-28
    说明：函数
"""

# def sum( arg1, arg2 ):
#     # 返回2个参数的和."
#     total = arg1 + arg2
#     print ("函数内 : ", total)
#     return total
#
# # 调用sum函数
# total = sum( 10, 20 )
# print ("函数外 : ", total)

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum( 10, 20 ))
print("相加后的值为 : ", sum( 20, 20 ))
