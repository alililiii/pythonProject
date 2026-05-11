#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: parts_saleData.py
@ Time: 2024/12/25 17:25
@ Author: lululi
@ version: python 3.8
@ Description: 绘制水管接头、打气泵继电器、节温器的销售数据图，三张图绘在一起
"""


import pandas as pd
import matplotlib.pyplot as plt
# 创建数据框
# 水管接头的销售数据
data1 = {
    'Week': range(34, 47),
    'Sales': [6, 8, 1, 11, 6, 5, 8, 5, 6, 3, 6, 3, 2]
}
df1 = pd.DataFrame(data1)

# 打气泵继电器的销售数据
data2 = {
    'Week': range(34, 47),
    'Sales': [2, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 1, 0]
}
df2 = pd.DataFrame(data2)

# 节温器的销售数据
data3 = {
    'Week': range(34, 47),
    'Sales': [7, 4, 6, 4, 7, 6, 5, 6, 6, 9, 9, 8, 5]
}
df3 = pd.DataFrame(data3)

# 绘制销售数据图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(18, 5))

# 把图纸分成一行3列
# 先画第一行第一列的图
plt.subplot(1, 3, 1)
plt.plot(df1['Week'], df1['Sales'], marker='o')
plt.title('水管接头销售数据')
plt.xlabel('周次')
plt.ylabel('销量')
# 再画第一行第二列的图
plt.subplot(1, 3, 2)
plt.plot(df2['Week'], df2['Sales'], marker='o', color='orange')
plt.title('打气泵继电器销售数据')
plt.xlabel('周次')
plt.ylabel('销量')
# 再画第一行第三列的图
plt.subplot(1, 3, 3)
plt.plot(df3['Week'], df3['Sales'], marker='o', color='green')
plt.title('节温器销售数据')
plt.xlabel('周次')
plt.ylabel('销量')

plt.tight_layout()
plt.show()
