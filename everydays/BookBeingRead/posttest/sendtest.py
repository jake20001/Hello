# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/2/5 11:01
# FileName : sendtest
# Description : 
# --------------------------------
import json

import requests


def request_function(Method,url):
    return requests.request(Method,url)


def main():
    response = request_function("GET","http://172.18.8.41:5000/response")
    print(response,type(response))
    print(response.text)


if __name__ == '__main__':
    main()