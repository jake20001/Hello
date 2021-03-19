# ///////////////////////////////////////////////////////////////////////////////////////////////  第一种思路
import time

s = "abccc"
t = list(s)


#
# def is_PalindromeString(t, oddnum):  # 判断是否是超赞字符串
#     for i in t:
#         if t.count(i) % 2 == 0:
#             popstring(i)
#             print(t)
#         else:
#             oddnum += 1
#             if oddnum > 1:
#                 break
#             popstring(i)
#             print(t)
#         is_PalindromeString(t, oddnum)
#         if not t:
#             return True
#     return False
#
#
# def popstring(i):  # 弹出字符串中的所有i
#     while t.count(i) != 0:
#         m = t.index(i)
#         t.pop(m)
#
#
# # print(is_PalindromeString(t, 0))


# ///////////////////////////////////////////////////////////////////////////////////////////////////// 第二种

def is_PalindromeString1(t):  # 判断是否是超赞字符串
    for i in t:
        if t.count(i) % 2 == 0:
            t = list(filter(lambda x: x != i, t))
        else:
            continue
    if len(set(t)) <= 1:
        return True
    else:
        return False


maxnum = 1


def longest(t):
    global maxnum
    for i in range(0, len(t) - maxnum):
        for j in range(maxnum, len(t) - i + 1):
            ss = t[i:i + j]
            if is_PalindromeString1(ss):
                maxnum = max(maxnum, j)

    return maxnum


start = time.time()
print("最长的超赞子字符串的长度为：", longest(t))
end = time.time()
print("花费时间：", start - end)
