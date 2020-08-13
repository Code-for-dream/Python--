#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/19 17:20
#!@Author: zyx
#!@File: .py
#numpy常用的统计函数
import numpy as np

t = np.arange(24).reshape((4,6))
print(t)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

print(t.sum(axis=0))
# [36 40 44 48 52 56]
print(t.sum(axis=1))
# [ 15  51  87 123]

print(t.mean(axis=0))
# [ 9. 10. 11. 12. 13. 14.]
print(t.mean(axis=1))
# [ 2.5  8.5 14.5 20.5]

#中值
print(np.median(t,axis=0))
# [ 9. 10. 11. 12. 13. 14.]
print(np.median(t,axis=1))
# [ 2.5  8.5 14.5 20.5]

print(t.max(axis=0))
#[18 19 20 21 22 23]
print(t.max(axis=1))
#[ 5 11 17 23]
print(t.min(axis=0))
#[0 1 2 3 4 5]
print(t.min(axis=1))
#[ 0  6 12 18]

#极值
print(np.ptp(t,axis=0))
# [18 18 18 18 18 18]
print(np.ptp(t,axis=1))
# [5 5 5 5]

#方差
print(t.std(axis=0))
#[6.70820393 6.70820393 6.70820393 6.70820393 6.70820393 6.70820393]
print(t.std(axis=1))
#[1.70782513 1.70782513 1.70782513 1.70782513]