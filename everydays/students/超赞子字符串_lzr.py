#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/11 20:18


def is_Palindrome(s):

    char_dict = {i: s.count(i) % 2 for i in s}

    char_odd = 0
    for i in char_dict.values():
        if i == 1:
            char_odd += 1

    if char_odd == 1 or char_odd == 0:
        return True
    # print(char_dict, char_odd)


def find(s):
    i = len(s)
    while i > 0:
        for j in range(len(s)-i):
            if is_Palindrome(s[j:j+i+1]):
                return len(s[j:j+i+1])
        i -= 1
    return s[0]


if __name__ == '__main__':
    s = 'abcccc'
    print('最长超赞子字符串长度：', find(s))