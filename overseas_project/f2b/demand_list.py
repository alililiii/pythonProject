#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: demand_list.py
@ Time: 2025/1/8 16:59
@ Author: lululi
@ version: python 3.8
@ Description: 构造询价需求列表数据
"""


import random
import json
import csv


# 构造询价需求列表，配件名称
def get_data(brandName, categoryName, num):

    original_items = []

    for i in range(num):

        original_item = {
          "brandIdDesc": random.choice(brandName),
          "description": random.choice(categoryName),
          "quantity": random.randint(0, 999999),
          "remark": "随机需求" + str(i),
          "resources": [
              {
                "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/zlb_rc-upload-1736817943333-7.bmp"
              },
              {
                "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/1656_rc-upload-1736817943333-9.jpeg"
              },
              {
                "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/2b_rc-upload-1736818271222-6.jpg"
              },
              {
                "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/1660_rc-upload-1736818271222-8.jpeg"
              },
              {
                "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/%E5%A5%94%E9%A9%B0-20240927-14_rc-upload-1736818271222-10.png"
              }
            ]
        }

        original_items.append(original_item)

    return original_items

    # # 将列表写入 JSON 文件
    # with open('demand_list.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(originalItems, json_file, ensure_ascii=False, indent=4)
    #
    # print("列表已写入 'demand_list.json'")


# 构造询价需求列表，零件号
def get_partNum(brandName, filename, num):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        # 创建csv读取器
        csv_reader = csv.reader(csvfile)
        original_items = []

        # enumerate()是Python中的一个内置函数，它为可迭代对象（如列表、元组、字符串等）提供一个索引计数器，返回一个包含索引和相应元素的可迭代对象。这使得你在遍历一个可迭代对象时，能够同时访问元素及其索引。
        # enumerate(i, j)，i表示可迭代对象，j表示索引计数的开始值，默认从0开始
        for i, row in enumerate(csv_reader, 1):
            original_item = {
                "brandIdDesc": random.choice(brandName),
                "description": row[0],
                "quantity": random.randint(0, 999999),
                "remark": "随机需求" + str(i),
                "resources": [
                    {
                        "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/zlb_rc-upload-1736817943333-7.bmp"
                    },
                    {
                        "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/1656_rc-upload-1736817943333-9.jpeg"
                    },
                    {
                        "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/2b_rc-upload-1736818271222-6.jpg"
                    },
                    {
                        "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/1660_rc-upload-1736818271222-8.jpeg"
                    },
                    {
                        "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/%E5%A5%94%E9%A9%B0-20240927-14_rc-upload-1736818271222-10.png"
                    }
                ]
            }

            original_items.append(original_item)

            # 读取指定行数据，到达指定行，退出循环
            if i == num - 1:
                break

        return original_items


