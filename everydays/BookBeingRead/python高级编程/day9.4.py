# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/17 18:05
# FileName : day9.4
# Description : 
# --------------------------------
import time
from queue import Queue
from multiprocessing import Pool

def set_data(*args,**kwargs):
    print("xxxx",args)
    print(kwargs)
    return kwargs

def set_data2(x):
    return x


def get_some(x):
    print('get some',x.values())
    time.sleep(1)

if __name__ == '__main__':
    q = Queue()
    q.put(1)
    # print(q.get_nowait())
    # l = [1,2,3]
    pool = Pool(processes=3)
    for i in range(2):
        if q.empty():
            break
        pool.apply_async(func=set_data,args=(1,),kwds={"aa":q.get_nowait()},callback=get_some)
    pool.close()
    pool.join()


# from multiprocessing import Pool
# import time
#
#
# def fun_01(i):
#     time.sleep(2)
#     print('start_time:', time.ctime())
#     return i + 100
#
#
# def fun_02(arg):
#     print('end_time:', arg, time.ctime())
#
#
# if __name__ == '__main__':
#     pool = Pool(3)
#     for i in range(4):
#         pool.apply_async(func=fun_01, args=(i,), callback=fun_02)  # fun_02的入参为fun_01的返回值
#         # pool.apply_async(func=fun_01, args=(i,))
#     pool.close()
#     pool.join()
#     print('done')