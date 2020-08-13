#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/6/14 11:03
#!@Author: zyx
#!@File: .py
#pandas
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置中文
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STXINGKA.TTF",size=18)

#读取csv文件
file_path = "911-calls/911.csv"
df = pd.read_csv(file_path)

#获取分类
temp_list = df["title"].str.split(":").tolist()
#分类在title字段中，这里将以：切分字符串并转化为list，每个元素类似于['EMS', ' SUBJECT IN PAIN']
cate_list = list(set(i[0] for i in temp_list))
#先遍历list，将第i个元素中的第一个子元素取出，就得到了每个元素的分类，再用set（）去重，最后转为list得到分类的列表
print(cate_list) #['Traffic', 'Fire', 'EMS']

#构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)

#赋值
#法一，遍历分类，为该分类的赋值
for cate in cate_list:
    zeros_df[cate][df["title"].str.contains(cate)] = 1
print(zeros_df)
#法二,逐行遍历赋值
# for i in range(df.shape[0]):
#     zeros_df.loc[i,temp_list[i][0]] = 1
# print(zeros_df)

sum_ret = zeros_df.sum(axis=0)
print(sum_ret)