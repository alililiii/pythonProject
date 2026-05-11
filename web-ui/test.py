#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: overseas.py
@ Time: 2025/3/21 17:10
@ Author: lululi
@ version: python 3.13
@ Description:2、开始自动化测试
"""


import pytest
import requests
import json


@pytest.mark.asyncio   # 标记这是一个异步测试
# @pytest.mark.parametrize("test_task,expected", [
#     ("""1、访问https://ec-hwbeta.casstime.com ,先点击账号登录,然后输入账号:ce01028622 密码:Init@1125 登陆后
# 2、进入https://ec-hwbeta.casstime.com/market/product/16357596427389470000/detail商品详情
# 3、点击立即购买，跳转到购物车页面
# 4、点击去结算，跳转到结算页
# 5、点击提交订单，跳转到收银台""", "收银台")
# ])
@pytest.mark.parametrize("test_task,expected", [
    ("""1、访问网址：https://if2b-beta.casstime.com/，输入账号：if2b_admin，密码：Cass1234，点击登录
    2、访问网址：https://if2b-beta.casstime.com/ru/mall
    3、配件目录页，点击购物车图标，进入购物车页面
    4、任意勾选一个商品，点击删除商品
    5、出现确认弹框，再点击确定
""", "删除商品")
])

async def test_run_task(test_task, expected):
    task_template = """
      你是一个自动化助手，需要完成以下任务：{test_task}，最后把页面看到的内容按照json格式返回
    """

    # 生成任务字符串，将参数值填充到模板中
    task = task_template.format(test_task=test_task,  expected=expected)

    # 构建请求数据
    request_data = {
        "task": task
    }

    try:
        # 向接口发送请求
        print(request_data)
        response = requests.post("http://127.0.0.1:5000/run-task", json=request_data)
        response.raise_for_status()

        # 解析响应数据
        result = response.json()

        # 检查响应中是否包含预期结果
        assert expected in str(result), f"预期 '{expected}' 未在输出中找到。"
    except requests.RequestException as e:
        pytest.fail(f"请求接口失败: {e}")
    except json.JSONDecodeError as e:
        pytest.fail(f"解析接口响应失败: {e}")

