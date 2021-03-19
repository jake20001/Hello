# -*- coding: utf-8 -*-
# n格阶梯，一步爬一个或者两格，求爬梯方案数


def path_way(n, s,step=3):
    global count

    if n < 0:
        return
    if n == 0:
        print(s)
        count += 1
        s.pop()
        print("========")
        return
    for i in range(1, step+1):
        print("ii",i)
        s.append(i)
        path_way(n-i,s,step)



if __name__ == '__main__':
    count = 0
    n = 3
    path_way(n,[])
    print(count)


