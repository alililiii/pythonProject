#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: save_image_from_url.py
@ Time: 2025/2/7 11:20
@ Author: lululi
@ version: python 3.8
@ Description: 读取图片url，下载并保存至文件夹
"""

import os
import requests
from PIL import Image
from io import BytesIO
import pandas as pd


def save_image_from_url(image_url, folder_path, file_name):
    # 创建文件夹（如果不存在的话）
    os.makedirs(folder_path, exist_ok=True)

    # 设置完整的文件保存路径
    save_path = os.path.join(folder_path, file_name)

    try:
        # 发送 GET 请求获取图片
        response = requests.get(image_url)
        response.raise_for_status()  # 检查请求是否成功

        # 使用 BytesIO 将响应内容转换为图片
        image = Image.open(BytesIO(response.content))

        # 根据图片格式决定保存的文件扩展名
        if image.format in ['JPEG', 'JPG']:
            file_extension = 'jpg'
        else:
            file_extension = image.format.lower()  # 其他格式使用小写

        # 更新保存路径包括扩展名
        save_path = os.path.splitext(save_path)[0] + '.' + file_extension

        # 保存图片
        image.save(save_path)
        print(f"图片已保存到 {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
    except IOError as e:
        print(f"保存图片时出错：{e}")


def download_images_from_csv(csv_path, folder_path, url_column):
    # 读取 CSV 文件
    try:
        data = pd.read_csv(csv_path)
        # print(data['pictureUrl'])

        # 确保指定的列存在
        if url_column not in data.columns:
            print(f"错误：CSV 文件中找不到列 '{url_column}'")
            return

            # 遍历 URL 列
        for index, row in data.iterrows():
            url = row[url_column]  # 获取当前行的 URL

            file_name = f"{row['partsNum']}"     # 用零件号当作图片名
            save_image_from_url(url, folder_path, file_name)

    except FileNotFoundError:
        print(f"错误：找不到文件 '{csv_path}'")
    except pd.errors.EmptyDataError:
        print("错误：CSV 文件为空")
    except Exception as e:
        print(f"发生了一个错误：{e}")


csv_path = 'MG1000.csv'  # CSV 文件路径
folder_path = 'images'  # 图片保存文件夹
url_column = 'pictureUrl'  # CSV 文件中包含图片 URL 的列名

download_images_from_csv(csv_path, folder_path, url_column)





