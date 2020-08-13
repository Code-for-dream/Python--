#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/8 9:52
#!@Author: zyx
#!@File: .py
#数组的计算
import numpy as np

t1 = np.arange(24)

#二维数组计算
t2 = t1.reshape((4,6))
print(t2)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]
#广播机制：可以应用到每一个元素上
t3 = t2+2  #加
print(t2)
# [[ 2  3  4  5  6  7]
#  [ 8  9 10 11 12 13]
#  [14 15 16 17 18 19]
#  [20 21 22 23 24 25]]
t4 = t2-2  #减
print(t4)
# [[-2 -1  0  1  2  3]
#  [ 4  5  6  7  8  9]
#  [10 11 12 13 14 15]
#  [16 17 18 19 20 21]]
t5 = t2*2  #乘
print(t5)
# [[ 0  2  4  6  8 10]
#  [12 14 16 18 20 22]
#  [24 26 28 30 32 34]
#  [36 38 40 42 44 46]]
t6 = t2/2  #除
print(t6)
# [[ 0.   0.5  1.   1.5  2.   2.5]
#  [ 3.   3.5  4.   4.5  5.   5.5]
#  [ 6.   6.5  7.   7.5  8.   8.5]
#  [ 9.   9.5 10.  10.5 11.  11.5]]
