#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Time:2020/5/25 21:44
# !@Author: zyx
# !@File: .py
# 2006-2016年1000部流行电影的数据，分理出评分的均分导演人数等数据
import numpy as np
import pandas as pd

# 读取外部CSV文件
file_path = "Topmovies/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
#查看数据总体信息
#print(df.info())
#查看第一条数据
#print(df.head(1))

#获取平均评分
print(df["Rating"].mean()) #6.723199999999999

#获取导演的人数
print(len(set(df["Director"].tolist()))) #644
#方法一
# 1.tolist() ---> Return a list of the values.   返回值列表
# 2.set()
#    def __init__(self, seq=()): # known special case of set.__init__
#         """
#         set() -> new empty set object
#         set(iterable) -> new set object
#
#         Build an unordered collection of unique elements. 建立独特元素的无序集合
#         # (copied from class doc)
#         """
#         pass
# 3.len()
#    def len(*args, **kwargs): # real signature unknown
#         """ Return the number of items in a container. """ 返回容器中的项目数
#         pass
#方法二
print(len(df["Director"].unique())) #644
# 1.unique() 该方法返回的是：去除目标列中重复值后的唯一值数组。本案例中就是返回所有导演名字的一个数组。
#    def unique(self):
#         """
#         Compute the ExtensionArray of unique values.  计算唯一值的扩展数组。
#
#         Returns
#         -------
#         uniques : ExtensionArray
#         """
#         uniques = unique(self.astype(object))
#         return self._from_sequence(uniques, dtype=self.dtype)

#获取演员的人数
temp_actors_list = df["Actors"].str.split(",").tolist()
actors_list = [i for j in temp_actors_list for i in j]
actors_num = len(set(actors_list))
print(actors_num) #2394

#获取电影时长的最大值、最小值
max_runtime = df["Runtime (Minutes)"].max()
print(max_runtime) #191
max_runtime_index = df["Runtime (Minutes)"].argmax()
print(max_runtime_index ) #828
min_runtime = df["Runtime (Minutes)"].min()
print(min_runtime) #66
min_runtime_index = df["Runtime (Minutes)"].argmin()
print(min_runtime_index ) #793
median_runtime = df["Runtime (Minutes)"].median()
print(median_runtime ) #111.0



