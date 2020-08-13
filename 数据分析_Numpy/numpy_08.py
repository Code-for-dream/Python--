#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/12 21:48
#!@Author: zyx
#!@File: .py
#布尔索引
import numpy as np

t1 = np.arange(24).reshape((4,6))
print(t1)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

print(t1<12)
# [[ True  True  True  True  True  True]
#  [ True  True  True  True  True  True]
#  [False False False False False False]
#  [False False False False False False]]

#把小于12的换为5
t1[t1<12] = 5
print(t1)
# [[ 5  5  5  5  5  5]
#  [ 5  5  5  5  5  5]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

