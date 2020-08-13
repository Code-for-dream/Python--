#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/25 14:32
#!@Author: zyx
#!@File: .py
#pandas数据缺失的处理
import pandas as pd
import numpy as np

d1 = [{"name":"张三","age":"20","tel":"10086"},{"name":"李四","tel":"10010"},{"age":"20"}]
t1 = pd.DataFrame(d1)
print(t1)
#   name  age    tel
# 0   张三   20  10086
# 1   李四  NaN  10010
# 2  NaN   20    NaN

#一、对nan值的判断
print(pd.isnull(t1))
#print(pd.isna(t1))
#     name    age    tel
# # 0  False  False  False
# # 1  False   True  False
# # 2   True  False   True
print(pd.notnull(t1))
#print(pd.notna(t1))
#     name    age    tel
# 0   True   True   True
# 1   True  False   True
# 2  False   True  False

#二、对nan值所在行或列的删除
#删除缺值行，axis=0
#注意：在默认情况下，how（删除方式）的默认值为any，即行中任何一列值为nan就删去该行
#可选项为all，只有当改行的每一列为nan时，才将改行删去
print(t1.dropna(axis=0))
#   name age    tel
#  0   张三  20  10086
print(t1.dropna(axis=0,how='any'))
#   name age    tel
# 0   张三  20  10086
print(t1.dropna(axis=0,how='all'))
#   name  age    tel
# 0   张三   20  10086
# 1   李四  NaN  10010
# 2  NaN   20    NaN

#inplace属性：决定是否将经过dropna方法处理后的数据代替原数据，默认值为False
print(t1)
#   name  age    tel
# 0   张三   20  10086
# 1   李四  NaN  10010
# 2  NaN   20    NaN
# t1.dropna(axis=0,how='any',inplace=True)
# print(t1)
#   name age    tel
# 0   张三  20  10086

#三、对数据为nan的填充
d2 = np.arange(24).reshape((6,4))
t2 = pd.DataFrame(d2)
print(t2)
#     0   1   2   3
# 0   0   1   2   3
# 1   4   5   6   7
# 2   8   9  10  11
# 3  12  13  14  15
# 4  16  17  18  19
# 5  20  21  22  23
t2.loc[[1,3,5],[0,1,3]] = np.nan
print(t2)
#       0     1   2     3
# 0   0.0   1.0   2   3.0
# 1   NaN   NaN   6   NaN
# 2   8.0   9.0  10  11.0
# 3   NaN   NaN  14   NaN
# 4  16.0  17.0  18  19.0
print(t2.mean())
# 0     8.0
# 1     9.0
# 2    12.0
# 3    11.0
# dtype: float64
print(t2.fillna(t2.mean())) #填充平均值,注意这一步不会对t2产生任何影响
#       0     1   2     3
# 0   0.0   1.0   2   3.0
# 1   8.0   9.0   6  11.0
# 2   8.0   9.0  10  11.0
# 3   8.0   9.0  14  11.0
# 4  16.0  17.0  18  19.0
# 5   8.0   9.0  22  11.0

d3 = [{"name":"zhangsan","age":20,"tel":10086},{"name":"lisi","tel":10010},{"name":"wangwu","age":20}]
t3 = pd.DataFrame(d3)
print(t3)
#        name   age      tel
# 0  zhangsan  20.0  10086.0
# 1      lisi   NaN  10010.0
# 2    wangwu  20.0      NaN
print(t3.mean()) #均值计算时不会将nan算进去
# age       20.0
# tel    10048.0
# dtype: float64
print(t3.fillna(t3.mean())) #实现所有nan之的一次性填充
#        name   age      tel
# 0  zhangsan  20.0  10086.0
# 1      lisi  20.0  10010.0
# 2    wangwu  20.0  10048.0
print(t3["age"].fillna(t3["age"].mean())) #实现对age一列的的单独填充
# 0    20.0
# 1    20.0
# 2    20.0
# Name: age, dtype: float64
t3["age"] = t3["age"].fillna(t3["age"].mean())
print(t3)
#        name   age      tel
# 0  zhangsan  20.0  10086.0
# 1      lisi  20.0  10010.0
# 2    wangwu  20.0      NaN

#处理为0的数据时：
#1.需要转化成nan，通过重新赋值---t[t==0]=np.nan 赋予nan值
#2.不需要转化时，保留原数据0.
#为什么要转化成nan？
#原因：在参与均值计算时，nan不参与，但是0会计入，导致均值的大小变化。









