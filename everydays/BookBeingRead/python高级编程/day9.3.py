# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/17 16:41
# FileName : day9.3
# Description : 
# --------------------------------
# import multiprocessing
from multiprocessing import Pool
from queue import Queue
# print('this machine has %d CPUs' % multiprocessing.cpu_count())


def add_data(q):
    for i in ('f1','f2','f3','f4'):
        q.put(i)
    return q

def worker(q):
    file = q.get()
    print("11111111111",'file',q)
    return 'worked on '


if __name__ == '__main__':
    q = Queue()
    add_data(q)
    # while not q.empty():
    #     worker(q)
    pool = Pool(processes=3)
    print(q.qsize())
    while not q.empty():
        print(q.qsize())
        result = pool.apply_async(worker,(q,))
        print(result.get(timeout=1))
    pool.close()
    pool.join()

# while True:
#     try:
#         result = pool.apply_async(worker)
#         # print(result.get(timeout=1))
#     except:
#         break
#
# pool.close()
# pool.join()


# import multiprocessing
# import time


# def func(msg):
#     print("msg:", msg)
#     time.sleep(3)
#     print("end,", msg)
#
# if __name__ == "__main__":
#     # 这里设置允许同时运行的的进程数量要考虑机器cpu的数量，进程的数量最好别小于cpu的数量，
#     # 因为即使大于cpu的数量，增加了任务调度的时间，效率反而不能有效提高
#     pool = multiprocessing.Pool(processes = 3)
#     item_list = ['processes1' ,'processes2' ,'processes3' ,'processes4' ,'processes5' ]
#     count = len(item_list)
#     for item in item_list:
#         msg = "hello %s" %item
#         # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
#         pool.apply_async(func, (msg,))
#
#     pool.close()
#     pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束