#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/19 18:31
#!@Author: zyx
#!@File: .py
#关于numpy中的nan
import numpy as np

#创建数组
t = np.arange(12).reshape((3,4)).astype("float")

#将部分数换为nan
t[1,2:] = np.nan
#print(t)
# [[ 0.  1.  2.  3.]
#  [ 4.  5. nan nan]
#  [ 8.  9. 10. 11.]]

def fill_ndarray(t):
    for i in range(t.shape[1]):  #遍历每一列
        temp_col = t[:,i] #当前的一列
        nan_num = np.count_nonzero(temp_col!=temp_col)
        if nan_num !=0:  #不为0，说明当前列中含有nan
           temp_not_nan_col = temp_col[temp_col==temp_col] #当前一列不为nan的array
           #选中当前为nan的位置，把值赋为不为nan的均值
           temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t

if __name__=='__main__':
    # 创建数组
    t1 = np.arange(12).reshape((3, 4)).astype("float")
    t1[2,2:] = np.nan
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)

# [[ 0.  1.  2.  3.]
#  [ 4.  5.  6.  7.]
#  [ 8.  9. nan nan]]
# [[0. 1. 2. 3.]
#  [4. 5. 6. 7.]
#  [8. 9. 4. 5.]]

