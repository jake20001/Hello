#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/11 20:18

"""
题目：给定一个字符串s,返回s中最长的‘超赞子字符串‘的长度
    超赞子字符串需满足的条件：
        该字符串是s的一个非空子字符串
        进行任意次数的字符交换后，该字符串可以变成一个h回文字符串

思路：1.根据超赞字符串需要满足的条件推出超赞字符串是字符串内所有字符个数都为偶数或只有一个字符数为奇数，
    其余为偶数的字符串。由此编写is_Palindrome函数判断传入字符串是否为超赞字符串
    2.根据’最长‘编写find函数由长倒短取字符串s的子字符串，并调用is_Palindrome函数判断其是否为超赞字符串
"""


def is_Palindrome(s):

    char_dict = {}
    char_odd = 0
    for i in s:
        if i not in char_dict:
            char_dict[i] = s.count(i) % 2
            if char_dict[i]:
                char_odd += 1
                if char_odd > 1:
                    return
    return True

    # char_dict = {i: s.count(i) % 2 for i in s}
    #
    # char_odd = 0
    # for i in char_dict.values():
    #     if i == 1:
    #         char_odd += 1
    #
    # if char_odd == 1 or char_odd == 0:
    #     return True
    # print(char_dict, char_odd)


def find(s):
    i = len(s)
    while i > 0:
        for j in range(len(s)-i+1):
            if is_Palindrome(s[j:j+i]):
                return len(s[j:j+i])
        i -= 1
    return 1


if __name__ == '__main__':
    s = 'abccc'
    print('最长超赞子字符串长度：', find(s))
