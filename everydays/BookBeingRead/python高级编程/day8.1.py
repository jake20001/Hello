# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/15 20:30
# FileName : day8.1
# Description : 
# --------------------------------
import unittest

def avarage(*numbers):
    numbers = [float(number) for number in numbers]
    return sum(numbers)/len(numbers)

class UtilsTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(avarage(1,2,3),2)
        self.assertEqual(avarage(1,2,3),1)

if __name__ == '__main__':
    unittest.main()
