#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/14 21:13
#!@Author: zyx
#!@File: .py
#复制与指代
import numpy as np

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9 ]

b = a #进行赋值操作
print(b)
# [0 1 2 3 4 5 6 7 8 9]


#返回指代
m = np.arange(12).reshape(4,3)
print(m)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

n = m.view()
print(n is m)
# False
n[0,2] =1314

print(m)
# [[   0    1 1314]
#  [   3    4    5]
#  [   6    7    8]
#  [   9   10   11]]


#深度复制
z = np.arange(12).reshape((3,4))

y = z.copy()
print(y.base is z)
# False

y[0,0] = 100
print(z)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(y)
# [[100   1   2   3]
#  [  4   5   6   7]
#  [  8   9  10  11]]