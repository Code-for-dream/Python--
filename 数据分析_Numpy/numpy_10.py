#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/13 15:48
#!@Author: zyx
#!@File: .py
#数据的拼接、分割   交换数据的行列
import numpy as np

t1 = np.arange(12).reshape((2,6))
print(t1)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]
t2 = np.array(range(12,24)).reshape((2,6))
print(t2)
# [[12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

#竖直拼接，注意竖直拼接的时候每一列代表的意义相同
t1_=np.vstack((t1,t2))
print(t1_)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

#水平拼接
t2_=np.hstack((t1,t2))
print(t2_)
# [[ 0  1  2  3  4  5 12 13 14 15 16 17]
#  [ 6  7  8  9 10 11 18 19 20 21 22 23]]

#假设t1、t2都是对不同两家店水果品种及存储量的记录，由于竖直拼接的时候每一列代表的意义相同，所以在t1、t2拼接时要进行列的交换
#t1["苹果","橘子","西瓜","榴莲","香蕉","葡萄"]
#t2["橘子","苹果","西瓜","榴莲","香蕉","葡萄"]
t2[:,[0,1]] = t2[:,[1,0]] #将t2的前两列进行交换
print(t2)
# [[13 12 14 15 16 17]
#  [19 18 20 21 22 23]]

#类似于列的交换，行也可以进行交换
t1[[0,1],:] = t1[[1,0],:] #将t1的一二两行进行交换
print(t1)
# [[ 6  7  8  9 10 11]
#  [ 0  1  2  3  4  5]]

t3 = np.arange(24).reshape((4,6))
print(t3)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]

