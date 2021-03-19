# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 14:21
# FileName : 006
# Description : 
# --------------------------------
# 与当前相差天数
import datetime
import time


def get_diff_days_2_now(date_str):
    now_time = time.localtime(time.time())
    compare_time = time.strptime(date_str, "%Y-%m-%d")
    # 比较日期
    date1 = datetime.datetime(compare_time[0], compare_time[1], compare_time[2])
    date2 = datetime.datetime(now_time[0], now_time[1], now_time[2])
    diff_days = (date2 - date1).days

    # 上面是正确的获取方法，返回一个int类型天差值，修改时间：2019年8月25日
    # diff_days = str(date2 - date1)
    # # 如果相差0天单纯显示为 00:00:00 不然显示为 [diff_days] : 00:00:00
    # diff_days_arr = diff_days.split(":")
    # if len(diff_days_arr) == 1:
    #     return 0
    # else:
    #     return diff_days_arr[0].split()[0]
    return diff_days

def get_diff_old_days_2_now(old_day,now_day):
    old_days = get_days(old_day)
    now_days = get_days(now_day)
    return (now_days - old_days).days

def get_days(old_day):
    old_day_struct = time.strptime(old_day, "%Y%m%d")
    days = datetime.datetime(old_day_struct[0], old_day_struct[1], old_day_struct[2])
    return days


def main():
    # print(get_diff_days_2_now('2020-10-31'))
    print(get_diff_old_days_2_now('20201031','20201101'))


if __name__ == '__main__':
    main()
