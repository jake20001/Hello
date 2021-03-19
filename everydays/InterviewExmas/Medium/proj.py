# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/9/16 16:37
# FileName : proj
# Description : 
# --------------------------------


def utf8test():
    # nstr = "下载开始"
    nstr = "ES11è½¯ä»¶çæ¬åå¸ç®¡æ§è¡¨_20200915.xlsx"
    print(nstr)
    x = nstr.encode('utf-8')
    y = x.decode('utf-8')
    print(x)
    print(y)

def main():
    utf8test()

if __name__ == '__main__':
    main()