# coding: utf-8
"""
    @author: zhangjk
    @file: str2excel.py
    @date: 2020-03-05
    说明：xxxx
"""
import os
import subprocess
import time


def f1():
    stream = subprocess.Popen('adb shell ls /data/tmp/dd', shell=True,stdout=subprocess.PIPE)
    while True:
        line = stream.stdout.readline().decode('utf-8','ignore').strip('\n').strip('\r').strip('\r')
        print(line)
        if line.find('No such file or directory')!=-1:
            os.system('adb shell mkdir /data/tmp/dd')
        if not line:
            break


def f2():
    logname = 'xlog_' + get_format_now_time()
    sor = 'sdcard/tencent/wecarspeech/log'
    resultStream = subprocess.Popen( "adb pull " + sor + " .\\" + logname, shell=True,stdout=subprocess.PIPE)
    while True:
        line = resultStream.stdout.readline().decode('utf-8','ignore').strip('\n').strip('\r')
        print("line",line)
        if not line:
            time.sleep(1)
            break

# 格式化成2016-03-20 11:45:39形式
def get_format_now_time():
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())


# f1()
f2()