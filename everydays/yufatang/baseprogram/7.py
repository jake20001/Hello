# coding: utf-8
"""
    @author: zhangjk
    @file: 7.py
    @date: 2020-02-28
    说明：堆，队列
"""

# 堆
def f1():
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)
    s = stack.pop()
    print(s)
    print(stack)
    s = stack.pop()
    print(s)
    s = stack.pop()
    print(s)
    print(stack)

# 队列
def f2():
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")           # Terry arrives
    queue.append("Graham")          # Graham arrives
    q = queue.popleft()                 # The first to arrive now leaves
    print(q)
    q = queue.popleft()                 # The second to arrive now leaves
    print(q)
    print(queue)                           # Remaining queue in order of arrival
    q1 = queue.pop()
    print(q1)
    print(queue)

def f3():
    from queue import LifoQueue
    queue = LifoQueue()
    queue.put('Java')
    queue.put('Python')
    queue.put('C')
    print(queue)
    while not queue.empty():
        print(queue.get())

def f4():
    from queue import SimpleQueue
    queue = SimpleQueue()
    queue.put('Java')
    queue.put('Python')
    queue.put('C')
    print(queue)
    while not queue.empty():
        print(queue.get())

def f5():
    from queue import PriorityQueue
    queue = PriorityQueue()
    queue.put('Java')
    queue.put('Python')
    queue.put('C')
    print(queue)
    while not queue.empty():
        print(queue.get())

def f6():
    from queue import Queue
    queue = Queue()
    queue.put('Java')
    queue.put('Python')
    queue.put('C')
    print(queue)
    while not queue.empty():
        print(queue.get())


# f1()
# f2()
# f3()
# f4()
# f5()
f6()