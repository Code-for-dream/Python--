#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/10 15:55
#!@Author: zyx
#!@File: .py
#本地数据的读取
#CSV：comma-separated value,逗号分隔值文件
# 显示：表格状态
#源文件：换行和逗号分隔行列的格式化文本，每一行的数据表示以条记录
import numpy as np

#设置frame
data_file_path = "../数据分析_numpy/data.csv"

t1 = np.loadtxt(data_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(data_file_path,delimiter=",",dtype="int")
print(t1)
print("*"*100)
print(t2)