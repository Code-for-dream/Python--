#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/8 9:01
#!@Author: zyx
#!@File: .py
#数组的形状
import numpy as np

#一维数组
t1 = np.arange(12)
print(t1) #[ 0  1  2  3  4  5  6  7  8  9 10 11]
print(t1.shape) #(12,) 表示该一维数组中的元素个数

#二维数组
t2 = np.array([[1,2,3],[4,5,6]])
print(t2) #[[1 2 3]
          # [4 5 6]]
print(t2.shape) #(2, 3) 表示2行3列

#三维数组
t3 = t1.reshape((2,2,3))
print(t3)
# [[[ 0  1  2]
#   [ 3  4  5]]
#
#  [[ 6  7  8]
#   [ 9 10 11]]]
print(t3.shape) #(2,2,3)


#修改数组形状

#低维到高维
#二维
t4 = t1.reshape((3,4))
print(t4) #[[ 0  1  2  3]
          # [ 4  5  6  7]
          # [ 8  9 10 11]]
print(t4.shape) #(3, 4)
#三维 假设定义24个数据
t5 = np.arange(24).reshape((2,3,4))
print(t5)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]
print(t4.shape) #(2, 3, 4) 2块,每块3行4列.

#高维到低维
t7 = np.arange(24).reshape((2,4,3)) #t7是一个三维数组
t8 = t7.reshape((24,))
print(t8) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
t9 = t7.reshape((t7.size,))
print(t9) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
t10 = t7.flatten() #直接展开
print(t10) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
#如果是二维转一维，还可以用（行数*列数）计算元素个数

#对t5修改形状
t6 = t5.reshape((4,6))
print(t6)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]
print(t5) #尽管通过t6对t5进行修改，但是t5本身不会变，它还是一个三维数组
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

t5 = t5.reshape((4,6)) #但是如果对t5本身进行修改，那么将改变t5原有的样式
print(t5)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]