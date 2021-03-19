# coding: utf-8
"""
    @author: zhangjk
    @file: 3.py
    @date: 2020-02-28
    说明：for while break continue
"""

def f1():
    while True:
        guess = input("请输入你的字母：")
        if guess == 'q':
            print("跳出循环")
            break
        print("output",guess)

def f2():
    ax = [x for x in range(10)]
    for i in ax:
        if i%2==0:
            continue
        print("输出奇数",i)


def main():
    # f1()
    f2()

if __name__ == '__main__':
    main()