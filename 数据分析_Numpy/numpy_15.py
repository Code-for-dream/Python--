#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/19 19:36
#!@Author: zyx
#!@File: .py
#nan的注意点
import numpy as np

#创建数组
t = np.arange(12).reshape((3,4)).astype("float")

t[2,2:] = np.nan
print(t)
# [[ 0.  1.  2.  3.]
#  [ 4.  5.  6.  7.]
#  [ 8.  9. nan nan]]

print(np.count_nonzero(t))
# 11

print(t!=t) #相当于print(np.isnan(t))
# [[False False False False]
#  [False False False False]
#  [False False  True  True]]

print(np.count_nonzero(t!=t))
# 2

