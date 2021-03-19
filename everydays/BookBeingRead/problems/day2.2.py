# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/2/3 19:42
# FileName : day1.3
# Description : 
# --------------------------------
import time
from concurrent.futures import as_completed,ThreadPoolExecutor



def fun(index):
    time.sleep(index+10)
    print("fun...",index)

args = [1,2,3]

with ThreadPoolExecutor(max_workers=2) as executor:
    # 在这里你可以使用for循环来做，返回的是一个future对象
    future_list=[]
    for i in range(2):
        future = executor.submit(fun, args[i])
        print('Scheduled for {}'.format(future)) # 查看future状态
        future_list.append(future)

    for t in future_list:
        print("111111111",t.done(),t._state)
        print('middle Scheduled for {}'.format(future))

    for res in as_completed(future_list,100): #这个futrure_list是你future对象的列表
        print('222222222',res)
        print(res._state)
        print(res.result())        #循环遍历时用.result()来取返回值
        print('end Scheduled for {}'.format(future))

    # executor.shutdown()

    for t in future_list:
        print("333333333",t.done(),t._state)


