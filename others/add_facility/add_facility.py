#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: add_facility.py
@ Time: 2025/2/25 9:34
@ Author: lululi
@ version: python 3.8
@ Description: 
"""


import requests
import csv
import random

# beta环境访问地址
base_url = 'https://ec-hwbeta.casstime.com'

url = '/merchant/system/storeFacility/query'

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    # beta-已登录
    'Cookie': 'did=01eeeb51-0f70-49fc-a76c-95e5e6b43391; gr_user_id=9069ba4a-4073-4984-9d63-677bded2bf63; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22mandy%22%2C%22first_id%22%3A%22194306491bf21de-0fdddddddddddd8-26011851-2073600-194306491c028bf%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22194306491bf21de-0fdddddddddddd8-26011851-2073600-194306491c028bf%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk0MzA2NGVmYzI0NWUtMGQ0MTlkODg3NjhkYmItMjYwMTE4NTEtMjA3MzYwMC0xOTQzMDY0ZWZjMzJkZmQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiJtYW5keSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22mandy%22%7D%7D; \143\150\145\143\153\123\145\164\164\154\145\151\156=\164\162\165\145; ssoToken=YTA0NzY0fDE3NDA0NDU4MDUAjHBZZ/5gcKs8YQkxn2ZUJg9xjn4p7jN/t1IIXnq9A2m9tSVCiHCi+joZQjqNfVD/9Y+6rSGQFFYkZKnKNcTCrdP4/fi2HqqFxWeTGKTkim8=; HWWAFSESID=5677f73bc99fd66391; HWWAFSESTIME=1740446106578; WSESSIONID=ff0175ee-c87e-440f-bd3a-bc88babb8a24; 9d2350559e69271a_gr_session_id=0c2af8cf-9633-478f-b275-9c60b87619e9; adv-statistics=%5B%7B%22code%22%3A%22undefined%22%2C%22id%22%3A%221796333722270420992%22%2C%22displayNum%22%3A1%7D%5D; 9d2350559e69271a_gr_session_id_sent_vst=0c2af8cf-9633-478f-b275-9c60b87619e9; PSESSIONID=6329fa33-3c40-46e2-b290-9dcb92a6fa70; ssoAuthCode=GQV7A1; company_id=10424; security_context=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjYXNzbWFsbC5jb20iLCJzdWIiOiJtYW5keSIsImdyb3VwVXNlciI6ImZhbHNlIiwicmVwcmVzZW50YXRpdmVDb21wYW55SWQiOiIxMDQyNCIsInJlZ2lzdGVyQ29tcGxldGVkIjoidHJ1ZSIsImNvbXBhbnlUeXBlIjoiU1VQUExJRVIiLCJjcmVkZW50aWFsc05vbkV4cGlyZWQiOiJ0cnVlIiwiYWRkaXRpb25hbEluZm8iOiJ7YWNjb3VudElkPTVmMTE4MDRjNGU2OTcxMDAwMTM3MjA1N30iLCJhY2NvdW50Tm9uRXhwaXJlZCI6InRydWUiLCJwcm9kdWN0U3RvcmVJZCI6IlNVUEVSMDA3IiwiZW5hYmxlZCI6InRydWUiLCJ1c2VybmFtZSI6Im1hbmR5IiwiYWNjb3VudE5vbkxvY2tlZCI6InRydWUiLCJhbmQiOiJjYXNzbWFsbCIsImp0aSI6ImFNYzJoUlYxcjRHakFqNGRLUTVQVFZMZk8zdGphaFVNIiwiaWF0IjoxNzQwNDQ2MTA5LCJleHAiOjE3NDA0ODIxMDh9.LvbadokZSj6R45EQAkfOUrNRPNfg-okK6WiSv5Efn4PM0ez_m8dZ9BvwFc8d0c8zA61X_TZt8MeDC1vk6cskbQ6Vdyw80uF6Ef5cXMnBPC-VLftt8cjLGWrj1lxMjDXRvqEcgZFwGOsZPUyqyEBTUS-73rCum5nuZUS3ldqV-Ng; security_userid=mandy; _admin_active_menu_id_=product_store_list; _admin_active_menu_url_=/admin/vip#/store/list'
}

csv_file = 'facilityID.csv'
# csv_headers = ["partsNum", "partsBrandName", "productId", "pictureUrl"]
csv_headers = ["facilityId"]


with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
    # 写入标题
    writer = csv.writer(f)
    writer.writerow(["facilityId"])

    try:
        # 发送 post 请求
        res = requests.get(url=base_url + url, headers=headers)
        # res = requests.post(url=base_url + url, json=data)

        if res.status_code == 200:
            print("成功获取仓库id")
            try:
                json_data = res.json()['data']['data']
                # print(json_data)

                for item in json_data:
                    writer.writerow([item["facilityId"]])

            except ValueError as e:
                print(f"解析JSON失败，可能不是有效的JSON格式: {e}")

        else:
            print(f"请求失败:{res.status_code}")

    except Exception as e:
        print(f"请求失败：{e}")




