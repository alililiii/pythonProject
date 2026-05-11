#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: basic.py
@ Time: 2025/1/10 10:27
@ Author: lululi
@ version: python 3.8
@ Description: 获取品牌、品类等基础信息
"""
import json
import random

import requests
from bs4 import BeautifulSoup


# 登录（获取的cookie不全，不能用）
def login(base_url, username, password):
    """
        该函数用于登录指定的登录接口并获取 cookie
        :param base_url: 登录接口的 URL
        :param username,password: 登录所需的用户名和密码
        :return: 包含 cookie 的会话对象，如果登录失败则返回 None
    """
    # 创建一个会话对象
    session = requests.session()
    # post请求的url和数据
    url = '/passport/login'
    data = {
        "logintype": "PASSWORD",
        "msg": "",
        "username": username,
        "password": password,
        "cellphone": "",
        "verifycode": ""
    }
    try:
        # 发送post请求
        response = session.post(url=base_url + url, data=data)

        # 检查登录请求是否成功（状态码 200 表示成功）
        response.raise_for_status()
        print("登录成功，已获取 cookie")
        return session

    except requests.exceptions.HTTPError as http_err:
        print(f"登录时发生 HTTP 错误: {http_err}")
    except Exception as err:
        print(f"登录时发生其他错误: {err}")
    return None


# 获取标准品牌
def get_brands(base_url, headers):
    url = '/supply-web/list/supply/car/brand'

    try:
        res = requests.get(base_url + url, headers=headers)

        if res.status_code == 200:
            data = res.json()
            # 获取品牌cod、品牌名称
            brand_codes = [brand_code['brandCode'] for brand_code in data['data']['brands']]
            brand_names = [brand_name['brandName'] for brand_name in data['data']['brands']]
            # print(brand_names)

            return brand_codes, brand_names
        else:
            print(f"标准品牌接口请求失败，状态码：{res.status_code}")
    except Exception as e:
        print(f"获取标准品牌发生错误：{e}")


# 获取标准配件名称
def get_std_names(base_url, session, keyword):
    url = '/supply-web/quotation/fuzzy/std-names'
    data = {
        "keyword": keyword,
        "languageCode": "zh_CN"
    }

    try:
        # response = requests.post(base_url + url, json=data, headers=headers)
        res = session.post(base_url + url, json=data)
        # 检查请求 GET 接口是否成功
        res.raise_for_status()
        print("成功访问 GET 接口，响应内容如下：")
        print(res.text)

        if res.status_code == 200:
            data = res.json()
            # print(data['data']['stdNames'][0]['stdName'])
            # 提取配件名称、配件code、标明code
            std_names = [std_name['stdName'] for std_name in data['data']['stdNames']]
            # print("222")
            category_codes = [category_code['categoryCode'] for category_code in data['data']['stdNames']]
            std_name_codes = [std_name_code['stdNameCode'] for std_name_code in data['data']['stdNames']]
            # print(std_names)

            return std_names, category_codes, std_name_codes
        else:
            print(f"标签配件名称接口请求失败，状态码：{res.status_code}")
    except Exception as e:
        print(f"获取标准配件名称发生错误：{e}")


# 查询四级品类列表
def get_categories():
    file_path = 'category_list.json'

    # 读取json文件
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # 读取全部行
        categories = [category['categoryName'] for category in data['data']['categories']]

    return categories
    # # 随机选择一行
    # random_line = random.choice(categories)
    #
    # # 打印随机选中的行
    # print("随机读取的行:", random_line.strip())


# base_url = 'https://f2b-beta.casstime.com'
# # 请求头
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#     'Content-Type': 'application/json;charset=UTF-8',
#     # beta-已登录
#     'Cookie': 'gr_user_id=b64f9c8d-b97c-4e15-897b-35eb34081053; \143\150\145\143\153\123\145\164\164\154\145\151\156=\164\162\165\145; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2266d96c5477a457000151eb71%22%2C%22first_id%22%3A%22194401c26f6581-04f696b86eb001-26011851-1474560-194401c26f72748%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk0NDAxYzI2ZjY1ODEtMDRmNjk2Yjg2ZWIwMDEtMjYwMTE4NTEtMTQ3NDU2MC0xOTQ0MDFjMjZmNzI3NDgiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI2NmQ5NmM1NDc3YTQ1NzAwMDE1MWViNzEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2266d96c5477a457000151eb71%22%7D%7D; WSESSIONID=a8f2e4e2-c47d-4c45-8950-8edc7f096c55; PSESSIONID=153d13a1-90bf-4ab8-89b9-ae49821d2e6d; ssoAuthCode=8vC8lO; company_id=e86013288; security_context=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjYXNzbWFsbC5jb20iLCJzdWIiOiI2NmQ5NmM1NDc3YTQ1NzAwMDE1MWViNzEiLCJyZXByZXNlbnRhdGl2ZUNvbXBhbnlJZCI6ImU4NjAxMzI4OCIsInB1cmNoYXNlcklkIjoiRlBVMDIyNjc4IiwicmVnaXN0ZXJDb21wbGV0ZWQiOiJ0cnVlIiwiY3JlZGVudGlhbHNOb25FeHBpcmVkIjoidHJ1ZSIsImFkZGl0aW9uYWxJbmZvIjoie2FjY291bnRJZD02NmQ5NmM1NWZiMDIyZjAwMDFjMjJlNzh9IiwiYWNjb3VudE5vbkV4cGlyZWQiOiJ0cnVlIiwic3RvcmVJZCI6IkZTVDAyNzczNCIsImVuYWJsZWQiOiJ0cnVlIiwicGxhdGZvcm0iOiJGMkIiLCJ1c2VybmFtZSI6IjY2ZDk2YzU0NzdhNDU3MDAwMTUxZWI3MSIsImFjY291bnROb25Mb2NrZWQiOiJ0cnVlIiwiYW5kIjoiZjJiLWJldGEiLCJqdGkiOiJpdlBZdHhVajA1bmNvZzlCMnFvNHZKRTg1bnVVNjRyUyIsImlhdCI6MTczNjQ3MjMzNCwiZXhwIjoxNzM2NTA4MzMzfQ.POnJsNHA56BF8F0z7H1XbTinJpzSgyLRpsgZzPh3SuABrrwE1bXD47mYEpqZt-W9EhWJfW7aehYPSr5kM-gXzlUn2ljjWp80vFBj2O1Wa70N4D4Gopltstz6MiYZxA6KyRZj-MuGcD4Wf21aCMvnc8OjNWoJQJ_VeMLWls2HADs; security_userid=66d96c5477a457000151eb71; languageCode=zh_CN'
# }


# std_names, category_codes, std_name_codes = get_std_names(base_url, headers=headers, keyword="")
# get_categories()
# print(random.choice(categories))
