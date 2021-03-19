# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/15 20:43
# FileName : day8.2
# Description : 
# --------------------------------
import unittest

def average(*numbers):
    numbers = [float(number) for number in numbers]
    return sum(numbers)/len(numbers)

class MyTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average(1,2,3),2)

class MyTest2(unittest.TestCase):
    def test_another_test(self):
        self.assertEqual(average(1,2,3),1)

# def test_siute():
#     def suite(test_class):
#         return unittest.makeSuite(test_class)
#     suite = unittest.TestSuite()
#     suite.addTests((suite(MyTests),suite(MyTest2)))
#     return suite

def test_siute():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    test_cases = (MyTests,MyTest2)
    for test_case in test_cases:
        tests = loader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_siute')

