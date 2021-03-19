# coding: utf-8
"""
    @author: zhangjk
    @file: 15.py
    @date: 2020-03-07
    说明：xxxx
"""

def trycatch(func):
    def wrapper():
        return func()
    return wrapper

# def trycatch(arg):
#     def wrap(func):
#         def wrapper():
#             try:
#                 return func
#             except:
#                 return False
#         return wrapper
#     return wrap


@trycatch
def test_func():
    return 1/0

print(test_func())


# def f2():
#     try:
#         return 1/0
#     except:
#         return False
#
# print(f2())