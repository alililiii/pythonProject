#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: cassChoice_gui.py
@ Time: 2024/12/30 10:01
@ Author: lululi
@ version: python 3.8
@ Description: 
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# 定义 ChromeDriver 的服务路径，需根据实际情况修改
chrome_driver_path = '/sa/mall#/product/list?brandId=8&yearIds=%5B"163"%2C"164"%2C"165"%2C"166"%2C"167"%2C"168"%2C"169"%2C"170"%2C"171"%2C"172"%2C"173"%5D'

# 创建 ChromeDriver 服务
service = Service(chrome_driver_path)

# 启动 Chrome 浏览器
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get('https://if2b-beta.casstime.com')

# 等待 5 秒
time.sleep(5)

# 查找元素，这里使用元素的 id 查找
element = driver.find_element(By.ID, 'input')

# 在元素中输入文本
element.send_keys('Hello, World!')

# 提交表单
element.submit()

# 关闭浏览器
driver.quit()




