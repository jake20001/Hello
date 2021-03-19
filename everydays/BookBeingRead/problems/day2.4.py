# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/2/4 10:39
# FileName : day2.4
# Description : 
# --------------------------------
import time
from threading import Thread


class MyThread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        time.sleep(2)

    def is_sleeping(self):
        return not self.isAlive()  # You need to know also if you already started the thread


if __name__ == '__main__':
    mMyThread = MyThread()
    mMyThread.start()
    while True:
        print(mMyThread.is_sleeping())
        if mMyThread.is_sleeping():
            print("xxxxx",mMyThread.isAlive())
            break

