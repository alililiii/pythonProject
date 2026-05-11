#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: create_demand.py
@ Time: 2025/1/8 10:01
@ Author: lululi
@ version: python 3.8
@ Description: 代客询价
"""

import requests
import csv
import random
import demand_list, basic

# beta环境访问地址
base_url = 'https://f2b-beta.casstime.com'

username = '15820240905'
password = 'Cass1234'

# # 先登录，获取cookie(获取的cookie字段不全)
# session = basic.login(base_url, username, password)
# print(f"返回cookie的内容：session.cookies.get_dict()")

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    # beta-已登录
    'Cookie': 'gr_user_id=b64f9c8d-b97c-4e15-897b-35eb34081053; WSESSIONID=766954b2-ba5e-42c8-b0f0-88a223db8bc2; \143\150\145\143\153\123\145\164\164\154\145\151\156=\164\162\165\145; PSESSIONID=40977c91-e38d-448b-b34d-8d842256cfe5; ssoAuthCode=AfPtFg; company_id=e86013288; security_context=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjYXNzbWFsbC5jb20iLCJzdWIiOiI2NmQ5NmM1NDc3YTQ1NzAwMDE1MWViNzEiLCJyZXByZXNlbnRhdGl2ZUNvbXBhbnlJZCI6ImU4NjAxMzI4OCIsInB1cmNoYXNlcklkIjoiRlBVMDIyNjc4IiwicmVnaXN0ZXJDb21wbGV0ZWQiOiJ0cnVlIiwiY3JlZGVudGlhbHNOb25FeHBpcmVkIjoidHJ1ZSIsImFkZGl0aW9uYWxJbmZvIjoie2FjY291bnRJZD02NmQ5NmM1NWZiMDIyZjAwMDFjMjJlNzh9IiwiYWNjb3VudE5vbkV4cGlyZWQiOiJ0cnVlIiwic3RvcmVJZCI6IkZTVDAyNzczNCIsImVuYWJsZWQiOiJ0cnVlIiwicGxhdGZvcm0iOiJGMkIiLCJ1c2VybmFtZSI6IjY2ZDk2YzU0NzdhNDU3MDAwMTUxZWI3MSIsImFjY291bnROb25Mb2NrZWQiOiJ0cnVlIiwiYW5kIjoiZjJiLWJldGEiLCJqdGkiOiJCR1VQcWk4Y1dTdUduUEhJdGdXeU1pYXN6TnRPSzFzMSIsImlhdCI6MTczOTMyMjc5NCwiZXhwIjoxNzM5MzU4NzkzfQ.h08XNcBhUv5of5GaOk17s2lJbwz4xsI_-4t9L2jiV1igjQr5pROOPdSDKbKNQC0qB8MA2rLam4ecVuhGe37v3v2n0LzSV3ZKtrjibsQSCrNGKkeH-zji8B6VaGN-rIpthxDFCAJ9GZ8lPBTxHzaZQfBxfXgEeY9Zrs5VQkXE5AE; security_userid=66d96c5477a457000151eb71; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2266d96c5477a457000151eb71%22%2C%22first_id%22%3A%22194f7b7ad6f1f01-0566c04c69e9628-26011b51-1474560-194f7b7ad702322%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk0ZjdiN2FkNmYxZjAxLTA1NjZjMDRjNjllOTYyOC0yNjAxMWI1MS0xNDc0NTYwLTE5NGY3YjdhZDcwMjMyMiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjY2ZDk2YzU0NzdhNDU3MDAwMTUxZWI3MSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2266d96c5477a457000151eb71%22%7D%7D; languageCode=zh_CN'
}

# 生成随机询价需求
brand_codes, brand_names = basic.get_brands(base_url, headers)
# std_names, category_codes, std_name_codes = basic.get_std_names(base_url, headers=headers, keyword="")
categoryName = basic.get_categories()
# # 获取需求条目入参，配件名称
# originalItems = demand_list.get_data(brand_names, categoryName, 1000)
# 获取需求条目入参，零件号
originalItems = demand_list.get_partNum(brand_names, 'D:/Documents/pythonProject/overseas_project/beta_BWM1000.csv', 10)


data = {
  "if2bStoreCustomerVO": {
    "id": "38a0ba44475ff548ce615eff5b0e724a",
    "storeId": "FST027734",
    "if2bOrgId": "IFORG02552",
    "countryCode": "SA",
    "countryName": "沙特阿拉伯",
    "companyFullName": "自动化测试公司",
    "companyShortName": "自动化测试",
    "contactPerson": "自动化",
    "contactNumber": "",
    "emailAddress": "ddddd@111.com",
    "remark": "",
    "isEnabled": "",
    "createdBy": "66d96c5477a457000151eb71",
    "createdStamp": 1731067008000,
    "lastUpdatedBy": "66d96c5477a457000151eb71",
    "lastUpdatedStamp": 1736300480000
  },
  "currency": "CNY",
  "defaultLanguage": "zh_CN",
  "originalItems": originalItems,
  "remark": "",
  "source": "PC",
  "timeZone": "+0800",
  "attachments": []
}

url = '/supply-web/customer/demand/create'
# 提交代客询价
try:
    # 发送 post 请求
    res = requests.post(url=base_url + url, json=data, headers=headers)
    # res = requests.post(url=base_url + url, json=data)

    if res.status_code == 200:
        print("成功发布1条代客询价单")

    else:
        print(f"请求失败:{res.status_code}")

except Exception as e:
    print(f"请求失败：{e}")







"""
# 通过登录接口获取cookie访问代客询价接口失败，cookie获取不全

if session:
    try:
        # 假设的接口 b 的 URL
        url = '/supply-web/customer/demand/create'
        # 假设接口 b 需要 POST 请求，这里给出示例数据
        data = {
            "if2bStoreCustomerVO": {
                "id": "38a0ba44475ff548ce615eff5b0e724a",
                "storeId": "FST027734",
                "if2bOrgId": "IFORG02552",
                "countryCode": "SA",
                "countryName": "沙特阿拉伯",
                "companyFullName": "自动化测试公司",
                "companyShortName": "自动化测试",
                "contactPerson": "自动化",
                "contactNumber": "",
                "emailAddress": "ddddd@111.com",
                "remark": "",
                "isEnabled": "",
                "createdBy": "66d96c5477a457000151eb71",
                "createdStamp": 1731067008000,
                "lastUpdatedBy": "66d96c5477a457000151eb71",
                "lastUpdatedStamp": 1736300480000
            },
            "currency": "CNY",
            "defaultLanguage": "zh_CN",
            "originalItems": originalItems,
            "remark": "",
            "source": "PC",
            "timeZone": "+0800",
            "attachments": []
        }
        # 使用带有 cookie 的会话对象发送 POST 请求到接口 b
        res = session.post(base_url + url, data=data)
        # 检查请求接口 b 是否成功
        res.raise_for_status()
        # print(f"成功发布代客询价: {res.text}")
        # print(res.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"访问接口 b 时发生 HTTP 错误: {http_err}")
    except Exception as err:
        print(f"访问接口 b 时发生其他错误: {err}")
    finally:
        # 关闭会话
        session.close()
"""





