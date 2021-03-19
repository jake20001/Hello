# coding: utf-8

def min_path(a):

    global i, j, s, m

    if i == len(a) or j == len(a[i]):
        return

    if i == len(a)-1 and j == len(a[len(a)-1])-1:
        s += a[i][j]
        print(s)
        m = min(s, m)
        s -= a[i][j]
        return

    for n in range(2):

        s += a[i][j]
        if n == 0:
            i += 1
        else:
            j += 1

        min_path(a)
        if n == 0:
            i -= 1
        else:
            j -= 1
        s -= a[i][j]


if __name__ == '__main__':
    ax = [7,3,8,8,1,0,2,7,4,4,4,5,2,6,5]
    a = (
        [7],
        [3, 8],
        [8, 1, 0],
        [2, 7, 4, 4],
        [4, 5, 2, 6, 5],
    )
    i, j, s, m = 0, 0, 0, float('inf')
    min_path(a)
    print('最短路径：%d' % m)

