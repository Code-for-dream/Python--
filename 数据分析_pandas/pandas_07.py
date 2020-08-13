#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/6/9 20:59
#!@Author: zyx
#!@File: .py
import numpy as np
import pandas as pd

file_path = "starbucks/directory.csv"
df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

#按照国家来分类
grouped = df.groupby(by="Country") #这里的grouped是一个DataFrameGroupBy对象，可迭代
print(grouped)
# DataFrameGroupBy
# 可以进行遍历
# for i in grouped:
#     print(i)
#     print("*"*100) #返回一个两个元素的元组，第一个是国家（Country）,第二个是该国家下的所有数据，类型是dataframe
# ('AE',          Brand  Store Number  ... Longitude Latitude
# 1    Starbucks  22331-212325  ...     55.47    25.42
# 2    Starbucks  47089-256771  ...     55.47    25.39
# 3    Starbucks  22126-218024  ...     54.38    24.48
# 4    Starbucks  17127-178586  ...     54.54    24.51
# 5    Starbucks  17688-182164  ...     54.49    24.40
# ..         ...           ...  ...       ...      ...
# 140  Starbucks   34253-62541  ...     55.38    25.33
# 141  Starbucks   1359-138434  ...     55.38    25.32
# 142  Starbucks   34259-54260  ...     55.37    25.30
# 143  Starbucks   34217-27108  ...     55.48    25.30
# 144  Starbucks  22697-223524  ...     55.54    25.53
# [144 rows x 13 columns])

# 可以调用聚合函数
# print(grouped.count()) #会将每一列按照国家来进行进行统计
#          Brand  Store Number  Store Name  ...  Timezone  Longitude  Latitude
# Country                                   ...
# AD           1             1           1  ...         1          1         1
# AE         144           144         144  ...       144        144       144
# AR         108           108         108  ...       108        108       108
# AT          18            18          18  ...        18         18        18
# AU          22            22          22  ...        22         22        22
#         ...           ...         ...  ...       ...        ...       ...
# TT           3             3           3  ...         3          3         3
# TW         394           394         394  ...       394        394       394
# US       13608         13608       13608  ...     13608      13608     13608
# VN          25            25          25  ...        25         25        25
# ZA           3             3           3  ...         3          3         3
# [73 rows x 12 columns]
# print(grouped["Brand"].count()) #也可以对其中的一列进行统计
# AD        1
# AE      144
# AR      108
# AT       18
# AU       22
#       ...
# TT        3
# TW      394
# US    13608
# VN       25
# ZA        3
# Name: Brand, Length: 73, dtype: int64

#比较中国和美国的星巴克店数
country_count = grouped["Brand"].count()
print(country_count["US"])
print(country_count["CN"])

#具体了解到中国的每一个省份的星巴克店的数量
# china_data = df[df["Country"]=="CN"]
# grouped = china_data.groupby(by="State/Province").count()["Brand"]
# print(grouped) #数字代表中国的省份编码
# State/Province
# 11    236
# 12     58
# 13     24
# 14      8
# 15      8
# 21     57
# 22     13
# 23     16
# 31    551
# 32    354
# 33    315
# 34     26
# 35     75
# 36     13
# 37     75
# 41     21
# 42     76
# 43     35
# 44    333
# 45     21
# 46     16
# 50     41
# 51    104
# 52      9
# 53     24
# 61     42
# 62      3
# 63      3
# 64      2
# 91    162
# 92     13
# Name: Brand, dtype: int64

#按照多个条件进行分组
#同时按照国家和省份分组，就会有两个索引，返回的是Series
grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped)
# Country  State/Province
# AD       7                  1
# AE       AJ                 2
#          AZ                48
#          DU                82
#          FU                 2
#                            ..
# US       WV                25
#          WY                23
# VN       HN                 6
#          SG                19
# ZA       GT                 3
# Name: Brand, Length: 545, dtype: int64

#若想返回的是DataFrame
grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped1,type(grouped1))
print("*"*100)
grouped2 = df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
print(grouped2,type(grouped2))
print("*"*100)
grouped3 = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]
print(grouped3,type(grouped3))
#以上的三种方式结果均为下表
#                         Brand
# Country State/Province
# AD      7                   1
# AE      AJ                  2
#         AZ                 48
#         DU                 82
#         FU                  2
#                        ...
# US      WV                 25
#         WY                 23
# VN      HN                  6
#         SG                 19
# ZA      GT                  3
# [545 rows x 1 columns] <class 'pandas.core.frame.DataFrame'>