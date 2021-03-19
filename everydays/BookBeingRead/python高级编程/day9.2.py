# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/17 16:14
# FileName : day9.2
# Description : 
# --------------------------------
import logging
import subprocess
import time
from queue import Queue

q = Queue()
q.put('converter.py')
def index_file(filename):
    logging.info('indexing %s' % filename)
    f = open(filename)
    try:
        content = f.read()
        print(content)
        subprocess.call(['df','-h'])
        time.sleep(0.5)
    finally:
        f.close()

def worker():
    if True:
        # print(q.get())
        index_file(q.get())
        q.task_done()

worker()
