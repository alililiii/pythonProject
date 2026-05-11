#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: order.py
@ Time: 2025/3/19 16:42
@ Author: lululi
@ version: python 3.8
@ Description: 
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_add_to_cart():
    try:
        # 配置 WebDriver
        service = Service("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        # 1. 访问网站并登录
        driver.get("https://if2b-beta.casstime.com")
        print("已打开网站")

        # 切换国家/地区为俄罗斯
        country_selector = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "选择国家的CSS选择器"))
        )
        Select(country_selector).select_by_visible_text("俄罗斯")
        print("已切换地区为俄罗斯")

        # 点击去登录
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'去登录')]"))
        )
        login_button.click()

        # 输入登录信息
        username_input = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = driver.find_element(By.NAME, "password")
        
        username_input.send_keys("if2b_admin")
        password_input.send_keys("Cass1234")
        
        # 点击登录按钮
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        print("已完成登录")

        # 2. 搜索商品
        time.sleep(2)  # 等待页面加载
        search_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='搜索']"))
        )
        search_input.send_keys("YML-BR-902")
        
        search_button = driver.find_element(By.XPATH, "//button[contains(text(),'搜索')]")
        search_button.click()
        print("已执行搜索")

        # 3. 选择商品并加入购物车
        time.sleep(2)  # 等待搜索结果
        first_item_checkbox = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']"))
        )
        first_item_checkbox.click()

        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'加入购物车')]")
        add_to_cart_button.click()
        print("已添加商品到购物车")

        # 4. 进入购物车
        cart_icon = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-icon"))  # 根据实际购物车图标的类名调整
        )
        cart_icon.click()
        print("已进入购物车页面")

        # 5. 修改商品数量
        quantity_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
        )
        quantity_input.clear()
        quantity_input.send_keys("999")
        print("已修改商品数量为999")

        # 验证结果
        time.sleep(1)  # 等待数量更新
        updated_quantity = quantity_input.get_attribute("value")
        assert updated_quantity == "999", f"商品数量验证失败，实际数量为: {updated_quantity}"
        print("测试通过：商品数量已成功更新为999")

    except Exception as e:
        print(f"测试失败：{str(e)}")
    finally:
        # 截图保存测试结果
        driver.save_screenshot("test_result.png")
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    test_add_to_cart()



