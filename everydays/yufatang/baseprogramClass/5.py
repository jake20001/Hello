# coding: utf-8
"""
    @author: zhangjk
    @file: 5.py
    @date: 2020-02-29
    说明：数据压缩
"""
import zlib

def f1():
    s = b'life is too short , we must use the short life carefully and happyily,so use python at once!'
    print(len(s))
    print(s)
    checksum = zlib.crc32(s)
    print(checksum)
    # 压缩
    t = zlib.compress(s,5)
    print(len(t))
    print(t)
    checksum = zlib.crc32(s)
    print(checksum)
    # 解压
    z = zlib.decompress(t)
    print(len(z))
    print(z)
    checksum = zlib.crc32(s)
    print(checksum)

f1()
