# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/2/9 9:58
# FileName : day1.2
# Description : 
# --------------------------------
from datetime import datetime, timedelta

SECONDS_PER_DAY = 24 * 60 * 60

def sleep_time():
    curTime = datetime.now()
    desTime = curTime.replace(hour=4, minute=0, second=0, microsecond=0)
    delta = desTime - curTime
    skipSeconds = int(delta.total_seconds())
    if skipSeconds<0:
        skipSeconds = SECONDS_PER_DAY + skipSeconds
    return skipSeconds
