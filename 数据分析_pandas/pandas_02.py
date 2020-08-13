#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/22 21:53
#!@Author: zyx
#!@File: .py
#pandas之DataFrame
import pandas as pd
import numpy as np

#DataFrame对象既有行索引，又有列索引
#行索引，表明不同行，横向索引，叫index，0轴，axis=0
#列索引，表明不同列，纵向索引，叫columns，1轴，axis=1
t1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(t1)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

#通过index、columns属性设置行、列索引
# t1 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"),columns=list("WXYZ"))
# print(t1)
#    W  X   Y   Z
# a  0  1   2   3
# b  4  5   6   7
# c  8  9  10  11

#字典创建方式
d2 = {"name":["张三","李四","王五"],"age":["20","21","20"],"tel":["10086","10010","35699"]}
t2 = pd.DataFrame(d2)
print(t2)
#   name age    tel
# 0   张三  20  10086
# 1   李四  21  10010
# 2   王五  20  35699

d3 = [{"name":"张三","age":"20","tel":"10086"},{"name":"李四","tel":"10010"},{"age":"20","tel":"35699"}]
t3 = pd.DataFrame(d3)
print(t3)
#   name  age    tel
# 0   张三   20  10086
# 1   李四  NaN  10010
# 2  NaN   20  35699

#DataFrame的基础属性
print(t2.index)
# RangeIndex(start=0, stop=3, step=1)
print(t2.columns)
# Index(['name', 'age', 'tel'], dtype='object')
print(t2.values)
# [['张三' '20' '10086']
#  ['李四' '21' '10010']
#  ['王五' '20' '35699']]
print(t2.shape)
# (3, 3)
print(t2.dtypes)
# name    object
# age     object
# tel     object
# dtype: object
print(t2.ndim)
# 2
print(t2.head(2)) #显示前两行
#   name age    tel
# 0   张三  20  10086
# 1   李四  21  10010
print(t2.tail(2)) #显示后两行
#   name age    tel
# 1   李四  21  10010
# 2   王五  20  35699
print(t2.info()) #展示该DataFrame的具体信息
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   name    3 non-null      object
#  1   age     3 non-null      object
#  2   tel     3 non-null      object
# dtypes: object(3)
# memory usage: 200.0+ bytes
# None
print(t2.describe())
#        name age    tel
# count     3   3      3
# unique    3   2      3
# top      王五  20  10086
# freq      1   2      1

#DataFrame中的排序方法
t2 = t2.sort_values(by="age") #默认升序
print(t2)
#   name age    tel
# 0   张三  20  10086
# 2   王五  20  35699
# 1   李四  21  10010
t2 = t2.sort_values(by="age",ascending=False)
print(t2)
#   name age    tel
# 1   李四  21  10010
# 0   张三  20  10086
# 2   王五  20  35699

#pandas的切片操作注意
# - 方括号写数字，表示取行，对行进行操作
# - 方括号写字符串，表示取列，对列进行操作
print(t3[:2]) #从开始至第二行结束
#   name  age    tel
# 0   张三   20  10086
# 1   李四  NaN  10010
print(t3[2:]) #从第三行至最后
#   name age    tel
# 2  NaN  20  35699

print(t3["age"]) #取出纵索引为age的一列
# 0     20
# 1    NaN
# 2     20
# Name: age, dtype: object
print(type(t3["age"])) #该列的数据类型
# <class 'pandas.core.series.Series'>

print(t3[:2]["age"]) #取出1-2行，纵索引为age的一列
# 0     20
# 1    NaN
# Name: age, dtype: object

#优化行列的数据获取  -loc（标签索引行）  -iloc（位置获取行）
t1 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"),columns=list("WXYZ"))
print(t1)
#    W  X   Y   Z
# a  0  1   2   3
# b  4  5   6   7
# c  8  9  10  11
print(t1.loc["a","W"])
print(type(t1.loc["a","W"]))
# 0
# <class 'numpy.int32'>
print(t1.loc["c","Z"])
print(type(t1.loc["c","Z"]))
# 11
# <class 'numpy.int32'>
print(t1.loc[["a","b"],["Z","Y","X"]]) #获取多行多列数据
#    Z  Y  X
# a  3  2  1
# b  7  6  5
print(t1.loc["a":"c",["Y","Z"]]) #特殊情况：在loc中,["X":"Y",[]]里的Y可以取到
#     Y   Z
# a   2   3
# b   6   7
# c  10  11

# t1 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"),columns=list("WXYZ"))
# print(t1)
#    W  X   Y   Z
# a  0  1   2   3
# b  4  5   6   7
# c  8  9  10  11
print(t1.iloc[1:3,[2,3]])
#     Y   Z
# b   6   7
# c  10  11
print(t1.iloc[1:3,1:3])
#    X   Y
# b  5   6
# c  9  10




