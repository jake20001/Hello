# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/4/27 14:47
# FileName : 2
# Description : 生产者消费者
# --------------------------------

import threading
import time
import queue
queue = queue.Queue()
count = 0

#生产者线程 当队列中产品数量小于100时就每隔1秒向队列放5个产品
class producer(threading.Thread):
    def run(self):
        global queue
        global count

        while True:
            if queue.qsize() == 0:
                print('producer ...')
                break
            if queue.qsize() < 1:
                list = []
                for i in range(5):
                    count = count + 1

                    queue.put(count)
                    list.append(count)
                print("生产者生产了5个产品:{0}".format(list))
            else:
                print('生产者线程等待中。。。')

            time.sleep(1)
#消费者线程 当队列中产品数量大于50时就每隔1秒从队列中消费20个产品
class consumer(threading.Thread):
    def run(self):
        global queue

        while True:
            if queue.qsize()==0:
                print("consumer ...")
                break
            if queue.qsize() > 0:
                list = []
                for i in range(10):
                    msg = queue.get()
                    list.append(msg)
                print("消费者消费了：{0}".format(list))
            else:
                print('消费者线程{0}等待中。。。'.format(self.name))
            time.sleep(1)

#先在消息队列中放入50个初始产品
print("主线程放入初始产品:")
for i in range(1,51):
    count = count + 1
    queue.put(i)
    print(i,end=' ')
    if(i%25==0):
        print('\n')

#启动生产者线程
p1 = producer()
p1.start()
p2 = producer()
p2.start()

#启动消费者线程
c1 = consumer()
c1.start()