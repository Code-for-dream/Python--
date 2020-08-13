#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/10 16:37
#!@Author: zyx
#!@File: .py
#关于转置
import numpy as np

t = np.arange(24).reshape((4,6))
print(t)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]
#法一
t1=t.transpose()
print(t1)
print("*"*15)

#法二
t2=t.swapaxes(1,0)
print(t2)
print("*"*15)

#法三
t3=t.T
print(t3)
print("*"*15)