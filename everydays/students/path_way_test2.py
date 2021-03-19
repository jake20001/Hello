# -*- coding: utf-8 -*-
# n格阶梯，一步爬一个或者两格，求爬梯方案数

import time


def path_way(n, step_len=3):

    global count, step_list

    if n < 0:
        return

    if n == 0:
        count += 1
        step_print()
        return

    for i in range(1, step_len+1):
        step_list.append(i)
        print("xxxx",n)
        path_way(n-i)
        step_list.pop()


def step_print():
    for i in step_list:
        print(i, end=" ")
    print()


def main():
    pass


if __name__ == '__main__':
    start_time = time.time()
    count = 0
    step_list = []
    path_way(3)
    end_time = time.time()
    print("方法总数：%d" % count)
    print("执行时间：", end_time-start_time)