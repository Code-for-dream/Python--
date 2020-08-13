#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/6/19 10:24
#!@Author: zyx
#!@File: .py
#统计出不同月份的不同类型的拨号次数的情况
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置中文
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simfang.ttf",size=18)

#读取csv文件
file_path = "911-calls/911.csv"
df = pd.read_csv(file_path)

#把时间字符串转化为时间类型设置为索引
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

#添加列，表示分类
temp_list = df["title"].str.split(":").tolist()
cate_list = [i[0] for i in temp_list]
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0]),1))
df.set_index("timeStamp",inplace=True)

# 设置图像大小
plt.figure(figsize=(20, 8), dpi=80)

#分组
for group_name,group_data in df.groupby(by="cate"):
    #对不同的分类进行绘图
    count_by_month = group_data.resample("M").count()["title"]

    _x = count_by_month.index
    _y = count_by_month.values
    _x = [i.strftime("%Y/%m/%d") for i in _x]

    # 绘图
    plt.plot(range(len(_x)), _y, label=group_name)

#设置坐标及图示
plt.xticks(range(len(_x)),_x,rotation=45)
plt.xlabel("年/月/日",fontproperties=my_font)
plt.ylabel("911紧急拨号次数",fontproperties=my_font)
plt.title("不同月份的不同类型的911紧急拨号次数的情况",fontproperties=my_font)
plt.legend(loc="best")

# 设置网格
plt.grid(True, linestyle="-.", alpha=0.3)

# 展示
plt.show()
