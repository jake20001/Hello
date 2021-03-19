#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author:Aaron
@version: 1.0.0
@file: business.py
@time: 2020/9/20 10:39 PM
"""

pay = [100,58,57,55,51,44,99,11,9,88]
maxb = 0
buy = {}
for i in range(len(pay)):
    if max(pay[i:]) - pay[i] > maxb:
        maxb = max(pay[i:]) - pay[i]
        buy['in'] = pay[i]
        buy['out'] = max(pay[i:])
print(maxb)
print(buy)
