# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/3 16:56
# FileName : day3.3
# Description : 
# --------------------------------
from threading import RLock, Thread

lock = RLock()

def synchronized(function):
    def _synchronized(*args,**kwargs):
        lock.acquire()
        try:
            return function(*args,**kwargs)
        finally:
            lock.release()
    return _synchronized

@synchronized
def thread_write_safe():
    with open('1.txt','w') as fd:
        fd.write("11111"*10)
    return 'OK'

@synchronized
def thread_read_safe():
    with open('1.txt') as fd:
        print(fd.read())



if __name__ == '__main__':
    Thread(target=thread_write_safe).start()
    Thread(target=thread_read_safe).start()

