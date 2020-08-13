#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/30 16:22
#!@Author: zyx
#!@File: .py
#数据组合
import numpy as np
import pandas as pd

#创建三个数组
t1 = pd.DataFrame(np.ones((2,4)),index=["A","B"],columns=list("abcd"))
print(t1)
#      a    b    c    d
# A  1.0  1.0  1.0  1.0
# B  1.0  1.0  1.0  1.0
t2 = pd.DataFrame(np.ones((3,3)),index=["A","B","c"],columns=list("123"))
print(t2)
#      1    2    3
# A  1.0  1.0  1.0
# B  1.0  1.0  1.0
# c  1.0  1.0  1.0
t3 = pd.DataFrame(np.ones((3,3)),index=["0","1","2"],columns=list("123"))
print(t3)
#      1    2    3
# 0  1.0  1.0  1.0
# 1  1.0  1.0  1.0
# 2  1.0  1.0  1.0

#数据堆叠---简单的把两个数据对象堆叠在一起
print(pd.concat([t2,t3])) #列名相同对齐堆叠
#      1    2    3
# A  1.0  1.0  1.0
# B  1.0  1.0  1.0
# c  1.0  1.0  1.0
# 0  1.0  1.0  1.0
# 1  1.0  1.0  1.0
# 2  1.0  1.0  1.0
print(t2.append(t3))
#      1    2    3
# A  1.0  1.0  1.0
# B  1.0  1.0  1.0
# c  1.0  1.0  1.0
# 0  1.0  1.0  1.0
# 1  1.0  1.0  1.0
# 2  1.0  1.0  1.0
print(pd.concat([t1,t3])) #列名不同错开堆叠，空余部分nan之填补
#      a    b    c    d    1    2    3
# A  1.0  1.0  1.0  1.0  NaN  NaN  NaN
# B  1.0  1.0  1.0  1.0  NaN  NaN  NaN
# 0  NaN  NaN  NaN  NaN  1.0  1.0  1.0
# 1  NaN  NaN  NaN  NaN  1.0  1.0  1.0
# 2  NaN  NaN  NaN  NaN  1.0  1.0  1.0



# join（）
#以最前面的数据为基础，数据的合并默认情况下是把行索引相同的数据合并到一起
print(t1.join(t2)) #t1有两行，只合并数据的前两行
#      a    b    c    d    1    2    3
# A  1.0  1.0  1.0  1.0  1.0  1.0  1.0
# B  1.0  1.0  1.0  1.0  1.0  1.0  1.0
print(t2.join(t1)) #t2有三行，合并数据，缺少的用nan值填补
#      1    2    3    a    b    c    d
# A  1.0  1.0  1.0  1.0  1.0  1.0  1.0
# B  1.0  1.0  1.0  1.0  1.0  1.0  1.0
# c  1.0  1.0  1.0  NaN  NaN  NaN  NaN
print(t1.join(t3)) #数据的合并默认情况下是把行索引相同的数据合并到一起，不一样索引的用nan填充
#      a    b    c    d   1   2   3
# A  1.0  1.0  1.0  1.0 NaN NaN NaN
# B  1.0  1.0  1.0  1.0 NaN NaN NaN

#  merge（）
#按照指定的列把数据按照一定的方式合并
left = pd.DataFrame({"A":["A0","A1","A2","A3"],"B":["B0","B1","B2","B3"],"Key":["k0","k1","k2","k3"]})
right = pd.DataFrame({"C":["C0","C1","C2","C3"],"D":["D0","D1","D2","D3"],"Key":["k0","k1","k2","k3"]})
print(left)
#     A   B Key
# 0  A0  B0  k0
# 1  A1  B1  k1
# 2  A2  B2  k2
# 3  A3  B3  k3
print(right)
#     C   D Key
# 0  C0  D0  k0
# 1  C1  D1  k1
# 2  C2  D2  k2
# 3  C3  D3  k3
print(pd.merge(left,right,on="Key"))
#     A   B Key   C   D
# 0  A0  B0  k0  C0  D0
# 1  A1  B1  k1  C1  D1
# 2  A2  B2  k2  C2  D2
# 3  A3  B3  k3  C3  D3

left = pd.DataFrame({"A":["A0","A1","A2","A3"],"B":["B0","B1","B2","B3"],"Key1":["k0","k0","k1","k2"],"Key2":["k0","k1","k0","k1"]})
right = pd.DataFrame({"C":["C0","C1","C2","C3"],"D":["D0","D1","D2","D3"],"Key1":["k0","k1","k1","k3"],"Key2":["k0","k0","k0","k0"]})
print(left)
#     A   B Key1 Key2
# 0  A0  B0   k0   k0
# 1  A1  B1   k0   k1
# 2  A2  B2   k1   k0
# 3  A3  B3   k2   k1
print(right)
#     C   D Key1 Key2
# 0  C0  D0   k0   k0
# 1  C1  D1   k1   k0
# 2  C2  D2   k1   k0
# 3  C3  D3   k3   k0
print(pd.merge(left,right,on=["Key1","Key2"])) #默认how=“inner”
#     A   B Key1 Key2   C   D
# 0  A0  B0   k0   k0  C0  D0
# 1  A2  B2   k1   k0  C1  D1
# 2  A2  B2   k1   k0  C2  D2

print(pd.merge(left,right,on=["Key1","Key2"],how="left")) #左外连接
#     A   B Key1 Key2    C    D
# 0  A0  B0   k0   k0   C0   D0
# 1  A1  B1   k0   k1  NaN  NaN
# 2  A2  B2   k1   k0   C1   D1
# 3  A2  B2   k1   k0   C2   D2
# 4  A3  B3   k2   k1  NaN  NaN
print(pd.merge(left,right,on=["Key1","Key2"],how="right")) #右外链接
#      A    B Key1 Key2   C   D
# 0   A0   B0   k0   k0  C0  D0
# 1   A2   B2   k1   k0  C1  D1
# 2   A2   B2   k1   k0  C2  D2
# 3  NaN  NaN   k3   k0  C3  D3
print(pd.merge(left,right,on=["Key1","Key2"],how="inner")) #内连接---交集
#     A   B Key1 Key2   C   D
# 0  A0  B0   k0   k0  C0  D0
# 1  A2  B2   k1   k0  C1  D1
# 2  A2  B2   k1   k0  C2  D2
print(pd.merge(left,right,on=["Key1","Key2"],how="outer")) #外连接---并集
#      A    B Key1 Key2    C    D
# 0   A0   B0   k0   k0   C0   D0
# 1   A1   B1   k0   k1  NaN  NaN
# 2   A2   B2   k1   k0   C1   D1
# 3   A2   B2   k1   k0   C2   D2
# 4   A3   B3   k2   k1  NaN  NaN
# 5  NaN  NaN   k3   k0   C3   D3

#数据填充
s1 = pd.Series([2, np.nan, 4, np.nan], index=['A', 'B', 'C', 'D'])
s2 = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])

# 用 s2 中的数值来填充 s1
print(s1.combine_first(s2))
'''
A    2.0
B    2.0
C    4.0
D    4.0
dtype: float64
'''

df1 = pd.DataFrame({
    'X':[1, np.nan, 3, np.nan],
    'Y':[5, np.nan, 7, np.nan],
    'Z':[9, np.nan, 11, np.nan]
})
df2 = pd.DataFrame({
    'Z':[np.nan, 10, np.nan, 12],
    'A':[1, 2, 3, 4]
})
# 功能同样是填充
print(df1.combine_first(df2))
'''
     A    X    Y     Z
0  1.0  1.0  5.0   9.0
1  2.0  NaN  NaN  10.0
2  3.0  3.0  7.0  11.0
3  4.0  NaN  NaN  12.0
'''

