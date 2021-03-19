# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/2/3 19:29
# FileName : day2.1
# Description : 
# --------------------------------
from concurrent.futures.thread import ThreadPoolExecutor

itr_arg = [1,2,3]

def map_fun(index):
    print("excuting...",index)

with ThreadPoolExecutor(max_workers=2) as executor:
    result = executor.map(map_fun, itr_arg)
    '''map_fun：你传入的要执行的map函数
      itr_arg：一个可迭代的参数，可以是列表字典等可迭代的对象
      基本上和python的map函数一样
      注意result并不是你map_fun返回的结果，而是一个生成器，如果要从中去结果，你可以使用列表生成式或者其他你想使用的方法
    '''
    for res in result:
        print(res) #这个res就是你map_fun返回的结果，你可以在这里做进一步处理



