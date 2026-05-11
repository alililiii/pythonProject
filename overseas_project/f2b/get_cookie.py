#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: get_cookie.py
@ Time: 2025/2/12 17:31
@ Author: lululi
@ version: python 3.8
@ Description: 使用浏览器自动化工具查看接口完整cookie，，不太ok
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


login_url = "https://f2b-beta.casstime.com/passport/login"

# 创建 Chrome 浏览器实例
driver = webdriver.Chrome()
# 打开登录页面
driver.get(login_url)
# 输入用户名和密码并提交表单（根据实际页面元素修改）
username_input = driver.find_element(By.ID, "15820240905")
password_input = driver.find_element(By.ID, "Cass1234")
submit_button = driver.find_element(By.ID, "submit")
username_input.send_keys("15820240905")
password_input.send_keys("Cass1234")
submit_button.click()
# 获取 cookie 信息
cookies = driver.get_cookies()
print(cookies)
# 关闭浏览器
driver.quit()




