#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/27 21:52
#!@Author: zyx
#!@File: .py
#数据的合并和分组聚合----统计电影的分类情况
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 读取外部CSV文件
file_path = "Topmovies/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

#难点：由于每一部电影的分类都不是唯一的，比如：某一部电影既是科幻类，也是爱情类，这样子在统计的时候两分类都得加上去
#思路：重新构造一个全为零的数组，列名为分类，若某一条数据中出现过该分类，则对应列加1
#1.统计分类的列表
temp_genre_list = df["Genre"].str.split(",").tolist()
#列表嵌列表的形式
# [['Action', 'Adventure', 'Sci-Fi'], ['Adventure', 'Mystery', 'Sci-Fi'], ……]
genre_list = list(set([i for j in temp_genre_list for i in j]))
#返回出所有的电影类别
#['Adventure', 'Western', 'Comedy', 'Musical', 'Sci-Fi', 'Animation', 'Music', 'Action', 'Biography', 'War', 'Sport', 'Horror', 'Romance', 'Drama', 'Fantasy', 'Crime', 'Mystery', 'Family', 'Thriller', 'History']

#2.构造全为零的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
print(zero_df)
#     War  Family  Mystery  History  ...  Animation  Comedy  Romance  Thriller
# 0    0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# 1    0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# 2    0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# 3    0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# 4    0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# ..   ...     ...      ...      ...  ...        ...     ...      ...       ...
# 995  0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# 996  0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# 997  0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# 998  0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# 999  0.0     0.0      0.0      0.0  ...        0.0     0.0      0.0       0.0
# [1000 rows x 20 columns]

#3.给每个电影分类出现的位置赋值
for i in range(df.shape[0]):
    zero_df.loc[i,temp_genre_list[i]] = 1

print(df["Genre"].head(3))
print(zero_df.head(3))
#取前三行进行检验，（中间部分被省略）
# 0     Action,Adventure,Sci-Fi
# 1    Adventure,Mystery,Sci-Fi
# 2             Horror,Thriller
# Name: Genre, dtype: object
#    Drama  Sport  History  Romance  ...  Musical  Adventure  Action  Music
# 0    0.0    0.0      0.0      0.0  ...      0.0        1.0     1.0    0.0
# 1    0.0    0.0      0.0      0.0  ...      0.0        1.0     0.0    0.0
# 2    0.0    0.0      0.0      0.0  ...      0.0        0.0     0.0    0.0
# [3 rows x 20 columns]

#统计每个分类的和（每一列的和）
genre_count = zero_df.sum(axis=0)
genre_count = genre_count.sort_values()
print(genre_count)
# Musical        5.0
# Western        7.0
# War           13.0
# Music         16.0
# Sport         18.0
# History       29.0
# Animation     49.0
# Family        51.0
# Biography     81.0
# Fantasy      101.0
# Mystery      106.0
# Horror       119.0
# Sci-Fi       120.0
# Romance      141.0
# Crime        150.0
# Thriller     195.0
# Adventure    259.0
# Comedy       279.0
# Action       303.0
# Drama        513.0
# dtype: float64

#设置字体
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\STXINGKA.TTF",size=18)
#设置图形大小
plt.figure(figsize=(20,8),dpi=80)
#设置坐标轴
_x = genre_count.index
_y = genre_count.values
#设置坐标轴信息
plt.xlabel("电影分类",fontproperties=my_font)
plt.ylabel("电影数量（部）",fontproperties=my_font)
plt.title("1000部电影的分类统计情况",fontproperties=my_font)
#绘制图形
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
#添加网格
plt.grid()
#展示
plt.show()