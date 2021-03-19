# coding: utf-8
"""
    @author: zhangjk
    @file: str2excel.py
    @date: 2019-11-29
    说明：xxxx
    硬性规则：
变量名由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
大小写敏感（大写的a和小写的A是两个不同的变量）。
不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。
PEP 8要求：
用小写字母拼写，多个单词用下划线连接。
受保护的实例属性用单个下划线开头（后面会讲到）。
私有的实例属性用两个下划线开头（后面会讲到）。
"""

def mamual_year():
    while True:
        year = int(input('请输入年份: '))
        if year=='q':
            break
        # 如果代码太长写成一行不便于阅读 可以使用\或()折行
        is_leap = (year % 4 == 0 and year % 100 != 0 or
                   year % 400 == 0)
        print(is_leap)

count = 0
def run_year(year):
    global count
    #
    is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    print(year,' === ',is_leap)
    if is_leap:
        count += 1



def main():
    N=100
    for i in range(1+N,401+N):
        run_year(i)
    print(count)
    # mamual_year()


if __name__ == '__main__':
    main()