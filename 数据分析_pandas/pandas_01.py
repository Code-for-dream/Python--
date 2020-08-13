#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/19 20:40
#!@Author: zyx
#!@File: .py
#初学pandas
import string
import pandas as pd
import numpy as np

#创建序列
t1 = pd.Series([15,46,19,24,33])
print(t1)
#索引   数据
# 0    15
# 1    46
# 2    19
# 3    24
# 4    33
# dtype: int64

# t = pd.Series([15,46,19,24,33],index=["a","b","c","d","e"])
t2 = pd.Series([15,46,19,24,33],index=list("abcde"))
print(t2)
# a    15
# b    46
# c    19
# d    24
# e    33
# dtype: int64

#以字典形式创建（键-值）
temp_dict = {"name":"小明","age":20,"tel":10086}
t3 = pd.Series(temp_dict)
print(t3)
# name       小明
# age        20
# tel     10086
# dtype: object

t4 = {string.ascii_uppercase[i]:i for i in range(5)}
print(t4)
# {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
print(pd.Series(t4))
# A    0
# B    1
# C    2
# D    3
# E    4
# dtype: int64

#当重新指定索引时，新的索引不能与旧索引对应的数据为nan
t5 = pd.Series(t4,index=list(string.ascii_uppercase[3:8]))
print(t5)
# D    3.0
# E    4.0
# F    NaN
# G    NaN
# H    NaN
# dtype: float64

#切片、索引操作
print(t4["A"])
# 0
print(t3[["name","age"]])
# name    小明
# age     20
# dtype: object
print(t3[1])
# 20
print(t5[["D","E","F"]])
# D    3.0
# E    4.0
# F    NaN
# dtype: float64
print(t1[t1>20])
# 1    46
# 3    24
# 4    33
# dtype: int64

#取出序列的索引和值
print(t1.index)
# RangeIndex(start=0, stop=5, step=1)
print(t1.values)
# [15 46 19 24 33]

#序列的运算
s = pd.Series(np.arange(5),index=['a','b','c','d','e'])
print(s)
# a    0
# # b    1
# # c    2
# # d    3
# # e    4
# # dtype: int32
S = s[1:]+s[3:]
print(S)
# b    NaN
# c    NaN
# d    6.0
# e    8.0
# dtype: float64
