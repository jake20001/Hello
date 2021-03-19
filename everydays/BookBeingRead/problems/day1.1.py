# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/1/6 20:19
# FileName : day1.1
# Description : 线程多久能killed
# --------------------------------
import threading


class MyThread(threading.Thread):

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self) -> None:
        print("it is",self.name)
        print("=====<>====",self.is_alive())


def main():
    mMyThread = MyThread("AAA")
    mMyThread.start()
    mMyThread.join(1)
    print("=========<>=======",mMyThread.is_alive())
    while True:
        if not mMyThread.is_alive():
            break
        print("=========",mMyThread.is_alive())



if __name__ == '__main__':
    main()
