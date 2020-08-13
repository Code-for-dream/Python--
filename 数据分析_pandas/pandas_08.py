#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/6/10 21:32
#!@Author: zyx
#!@File: .py
#索引和复合索引
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(12).reshape((3,4)),index=(list("abc")),columns=(list("ABCD")))
print(df)
#    A  B   C   D
# a  0  1   2   3
# b  4  5   6   7
# c  8  9  10  11

print(df.index)
# Index(['a', 'b', 'c'], dtype='object')

df3 = df.reindex(list("abcd"))
print(df3)
#      A    B     C     D
# a  0.0  1.0   2.0   3.0
# b  4.0  5.0   6.0   7.0
# c  8.0  9.0  10.0  11.0
# d  NaN  NaN   NaN   NaN

#指定索引
df.index = ["a","b","m"]
print(df)
#    A  B   C   D
# a  0  1   2   3
# b  4  5   6   7
# m  8  9  10  11

#重新设置索引
print(df.reindex(list("abd")))
#      A    B    C    D
# a  0.0  1.0  2.0  3.0
# b  4.0  5.0  6.0  7.0
# d  NaN  NaN  NaN  NaN

#指定某一列为索引
print(df.set_index("A"))
#    B   C   D
# A
# 0  1   2   3
# 4  5   6   7
# 8  9  10  11
print(df.set_index("A",drop=False))
#    A  B   C   D
# A
# 0  0  1   2   3
# 4  4  5   6   7

#设置两个索引
df1 = df.set_index(["A","B"],drop=False)
print(df1)
#      A  B   C   D
# A B
# 0 1  0  1   2   3
# 4 5  4  5   6   7
# 8 9  8  9  10  11
print(df1.index)
# MultiIndex([(0, 1),
#             (4, 5),
#             (8, 9)],
#            names=['A', 'B'])

#设置三个索引
df2 = df.set_index(["A","B","C"],drop=False)
print(df2)
#         A  B   C   D
# A B C
# 0 1 2   0  1   2   3
# 4 5 6   4  5   6   7
# 8 9 10  8  9  10  11
print(df2.index)
# MultiIndex([(0, 1,  2),
#             (4, 5,  6),
#             (8, 9, 10)],
#            names=['A', 'B', 'C'])


a = pd.DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one','two','two','two','two'],'d':list("hjklmno")})
print(a)
#    a  b    c  d
# 0  0  7  one  h
# 1  1  6  one  j
# 2  2  5  one  k
# 3  3  4  two  l
# 4  4  3  two  m
# 5  5  2  two  n
# 6  6  1  two  o

b = a.set_index(["c","d"])
print(b)
#        a  b
# c   d
# one h  0  7
#     j  1  6
#     k  2  5
# two l  3  4
#     m  4  3
#     n  5  2
#     o  6  1

print(b.loc["one"].loc["h"])
# a    0
# b    7


c = b["a"]
print(c,type(c))
# c    d
# one  h    0
#      j    1
#      k    2
# two  l    3
#      m    4
#      n    5
#      o    6
# Name: a, dtype: int64 <class 'pandas.core.series.Series'>
#对于复合索引Series的切片操作
print(c["one"]["j"]) #1
print(c["one"])
# h    0
# j    1
# k    2
# Name: a, dtype: int64

#我们将c、d两列的顺序调换
d = a.set_index(["d","c"])["a"]
print(d)
#        a
# d c
# h one  0
# j one  1
# k one  2
# l two  3
# m two  4
# n two  5
# o two  6

#此时若要取内层索引为one的数据
#法一：以c["..."]的形式，将内层索引为one的一个一个取出
#法二：使用swaplevel()方法交换
e = d.swaplevel()
print(e)
# c   d
# one h  0
#     j  1
#     k  2
# two l  3
#     m  4
#     n  5
#     o  6
print(e["one"])
# d
# h    0
# j    1
# k    2
# Name: a, dtype: int64
print(e["one","h"])
# 0
