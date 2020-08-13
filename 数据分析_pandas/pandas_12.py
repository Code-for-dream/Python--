#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/6/16 8:52
#!@Author: zyx
#!@File: .py
#pandas 分组聚合
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
cate_list = [i[0] for i in temp_list]
#先遍历list，获取出第i个元素中的第一个子元素
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0]),1))
df["cate"] = cate_df #添加新的一列分类
print(df.groupby(by="cate").count()["title"])
