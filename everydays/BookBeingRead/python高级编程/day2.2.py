# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/2 20:31
# FileName : day2.2
# Description : 
# --------------------------------
import itertools


def starting_at_five():
    value = input().strip()
    while value!='':
        for el in itertools.islice(value.split(),4,None):
            yield el
        value = input().strip()

def with_head(iterable,headsize=1):
    a,b = itertools.tee(iterable)
    return list(itertools.islice(a,headsize)),b

def with_head2(iterable,headsize=1):
    a,b = itertools.tee(iterable)
    return list(itertools.islice(a,headsize)),list(itertools.islice(b,headsize))

def compress(data):
    return ((len(list(group)),name) for name,group in itertools.groupby(data))

def decompress(data):
    return (car*size for size,car in data)

def function():
    seq = [1,2]
    ichain = itertools.chain(seq)
    print(list(ichain))
    icount = itertools.count(1)
    print(next(icount))
    print(next(icount))


if __name__ == '__main__':
    # while True:
    #     iter = starting_at_five()
    #     print(next(iter))

    # seq = [1,2]
    # # print(with_head(seq))
    # print(with_head2(seq,4))

    # data = list(compress('get uuuuuuuuuuuu'))
    # print(data)
    # print(''.join(decompress(data)))

    function()



# ==========================
# sorted()
# ==========================