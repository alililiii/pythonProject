#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: decode_demand.py
@ Time: 2025/1/9 14:03
@ Author: lululi
@ version: python 3.8
@ Description: 提交译码需求
"""
import csv
import random
import string
import requests
import basic


# 生成随机零件号
def generate_random_string():
    # 定义可用字符集，包括大小写字母、数字、空格和短横线
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    characters = letters + string.digits + ' - '

    # 随机选择字符并生成字符串
    random_string = ''.join(random.choice(characters) for _ in range(11))
    part_number = random.choice(string.ascii_letters) + random_string
    # print(part_number)

    return part_number


# for _ in range(10):
#     generate_random_string()

# 读取标准oe
def get_part_num():

    parts_num = []
    with open('D:/Documents/pythonProject/overseas_project/products_beta.csv', newline='', encoding='utf-8') as file:
        read_line = csv.reader(file)

        for part in read_line:
            parts_num.append(part[0])

    return parts_num


# 获取待译码需求id
def get_part_id(base_url, headers, inquiry_number):
    # 获取译码详情接口
    url = '/supply-web/supply/demand/decode/read/' + inquiry_number

    try:
        # 发起GET请求
        response = requests.get(base_url + url, headers=headers)
        # print(response.text)

        # 检查请求是否成功
        if response.status_code == 200:
            # 获取出参（返回的内容）
            data = response.json()  # 如果返回的是JSON格式
            # 获取所有待译码需求id
            parts_id = [ids['id'] for ids in data['data']['originalItems']]
            # print(parts_id)
            return parts_id
        else:
            print(f"译码详情接口请求失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"获取译码详情接口发生错误：{e}")


# 构造译码入参
def get_original_items(base_url, headers, inquiry_number):

    parts_id = get_part_id(base_url, headers, inquiry_number)
    brand_codes, brand_names = basic.get_brands(base_url, headers)
    parts_number = get_part_num()
    std_names, category_codes, std_name_codes = basic.get_std_names(base_url, headers, keyword="")
    # categoryName = basic.get_categories()

    original_items = []

    for i in range(2, len(parts_id)):

        temp = random.choice(range(19))

        original_item = {
            "id": parts_id[i],
            "standardItems": [
                {
                    "brandId": random.choice(brand_codes),
                    # "partsNumber": generate_random_string(),
                    "partsNumber": random.choice(parts_number),
                    "standardNameCode": std_name_codes[temp],
                    "partsName": std_names[temp],
                    "categoryCode": category_codes[temp],
                    "remark": "译码备注",
                    "resources": [
                      {
                        "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/160_rc-upload-1736818271222-2.gif"
                      },
                      {
                        "resourceValue": "https://file-upload.cassmall.com/hwbeta/f2b/2025-01-14/1563_rc-upload-1736818271222-4.png"
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
                    ],
                    "clarifiedMethod": "MANUALLY"
                }
            ]
        }

        original_items.append(original_item)

    return original_items


# 提交译码结果
def decode_demand(base_url, headers, inquiry_number):
    # 提交译码需求接口
    url = '/supply-web/supply/demand/resolve'

    # 构造译码入参
    original_items = get_original_items(base_url, headers, inquiry_number)
    data = {
              "demandId": inquiry_number,
              "originalItems": original_items
            }

    try:
        # 发送post请求
        res = requests.post(base_url + url, json=data, headers=headers)

        if res.status_code == 200:
            print("请求成功")

        else:
            print("请求失败")

    except Exception as e:
        print(f"发生错误：{e}")


# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    # beta-已登录
    'Cookie': 'gr_user_id=b64f9c8d-b97c-4e15-897b-35eb34081053; \143\150\145\143\153\123\145\164\164\154\145\151\156=\164\162\165\145; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2266d96c5477a457000151eb71%22%2C%22first_id%22%3A%221944f90234c699-0228625393d743c-26011851-2073600-1944f90234d259d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk0NGY5MDIzNGM2OTktMDIyODYyNTM5M2Q3NDNjLTI2MDExODUxLTIwNzM2MDAtMTk0NGY5MDIzNGQyNTlkIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiNjZkOTZjNTQ3N2E0NTcwMDAxNTFlYjcxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2266d96c5477a457000151eb71%22%7D%2C%22%24device_id%22%3A%2219463550d10d73-0ba033b10ed1b78-26011851-2073600-19463550d112a41%22%7D; WSESSIONID=88865e2c-66a3-4341-96d2-14e22b329d90; PSESSIONID=66f14008-0a65-4856-9d9b-be2b0aded6b1; ssoAuthCode=FXnOKm; company_id=e86013288; security_context=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjYXNzbWFsbC5jb20iLCJzdWIiOiI2NmQ5NmM1NDc3YTQ1NzAwMDE1MWViNzEiLCJyZXByZXNlbnRhdGl2ZUNvbXBhbnlJZCI6ImU4NjAxMzI4OCIsInB1cmNoYXNlcklkIjoiRlBVMDIyNjc4IiwicmVnaXN0ZXJDb21wbGV0ZWQiOiJ0cnVlIiwiY3JlZGVudGlhbHNOb25FeHBpcmVkIjoidHJ1ZSIsImFkZGl0aW9uYWxJbmZvIjoie2FjY291bnRJZD02NmQ5NmM1NWZiMDIyZjAwMDFjMjJlNzh9IiwiYWNjb3VudE5vbkV4cGlyZWQiOiJ0cnVlIiwic3RvcmVJZCI6IkZTVDAyNzczNCIsImVuYWJsZWQiOiJ0cnVlIiwicGxhdGZvcm0iOiJGMkIiLCJ1c2VybmFtZSI6IjY2ZDk2YzU0NzdhNDU3MDAwMTUxZWI3MSIsImFjY291bnROb25Mb2NrZWQiOiJ0cnVlIiwiYW5kIjoiZjJiLWJldGEiLCJqdGkiOiJvVTc1TGhRR1BZcUxHbzQxeEZTOHU0U1lqcU1DY3BzSCIsImlhdCI6MTczNjk4OTcwNCwiZXhwIjoxNzM3MDI1NzAzfQ.oLPpQSJqKZf5b6FdVvxJRs7dh8v3EVXdlU5PKk9uze1O-tXIrXBecPP0sLc801csceVBrEVDm4SAjwGTX5Msd9ZJCxs3P_60ycT4A8gWX2Y2W_zJU0HXJVeohGU79q_MINPdSBOSGzf3k9i9VI_i9rxHwsoWhFOk4VRnCX57x-k; security_userid=66d96c5477a457000151eb71; languageCode=en_US'
}

# 要请求的接口url
base_url = 'https://f2b-beta.casstime.com'


# get_original_items(base_url, headers, "R25010802707")
decode_demand(base_url, headers, "R25011609025")


