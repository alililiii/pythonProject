#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ File: add_to_demandList.py
@ Time: 2024/11/7 13:45
@ Author: lululi
@ version: python 3.8
@ Description: 批量将catalog中配件目录商品加入需求清单，使需求清单内sku数达上线1000
"""
import requests
import csv

# beta环境访问地址
url_base = 'https://if2b-beta.casstime.com'
url = '/customer-web/customer/demand-list/need/operate'

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    # beta-未登录
    'Cookie': 'gr_user_id=ecbe2b91-b7bc-45b7-8218-a0104487ae2c; languageCode=zh_CN; company_id=; WSESSIONID=ea041b58-160a-4b0b-adac-872009a6ca81; ssoAuthCode=ziNKnM; security_context=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjYXNzbWFsbC5jb20iLCJzdWIiOiIwMDUiLCJhY2NvdW50SWQiOiI2NmYzZGQ3NGZiMDIyZjAwMDE2NjI1MWMiLCJjbGllbnRJZCI6ImlmMmIiLCJ1c2VybmFtZSI6IjAwNSIsImFuZCI6ImlmMmIiLCJqdGkiOiI1YlhJN0d0WGdVTmhCRzBQamoycFhuYkFTSWY4U2JYNSIsImlhdCI6MTczMDcwMjE1MSwiZXhwIjoxNzMwNzM4MTUwfQ.DNDiJILW0nxShLoL_N5WbAVbkhLmZim1wx0uzdg2VyQLbdenfs_8vcg9kEmDEzg0ChM-kT-D4ZNmxpp7hocQqCQawGG4LtFngJZbRg6-imU0UUYkJJZ5s5hTmJrUXT8yeDOl23SIbdQRzwN02d8KBDO5UA1CNslrb1Eq9EVQjRA; security_context_exp=1730738150; security_userid=005; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22005%22%2C%22first_id%22%3A%22192e6ce2bd93c1-0b24f1523e3a03-26011951-2073600-192e6ce2bda1b53%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyZTZjZTJiZDkzYzEtMGIyNGYxNTIzZTNhMDMtMjYwMTE5NTEtMjA3MzYwMC0xOTJlNmNlMmJkYTFiNTMiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIwMDUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22005%22%7D%7D'
}

with open('products_beta.csv', newline='', encoding='utf-8') as csvfile:
    # 创建csv读取器
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        print(row[0])

        # 拼接入参
        data = {
          "countryCode": "US",
          "demandListItemList": [
            {
              "productId": row[2],
              "partsNumber": row[0],
              "brandCode": "275",
              "qualityId": "OE"
            }
          ]
        }

        try:
            # 发送 post 请求
            res = requests.post(url=url_base + url, json=data, headers=headers)

            if res.status_code == 200:
                print("请求成功")

            else:
                print("请求失败")

        except Exception as e:
            print(f"请求失败：{e}")






