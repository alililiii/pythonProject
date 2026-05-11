#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: overseas.py
@ Time: 2025/3/22 17:10
@ Author: lululi
@ version: python 3.13
@ Description: 
"""

from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio, os
from dotenv import load_dotenv


# 加载环境变量
load_dotenv()
async def main():
    # 初始化DeepSeek V3模型
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat',
        api_key=os.environ.get('DEEPSEEK_API_KEY')  # 替换为实际API密钥
    )

    agent = Agent(
        task="""
        1. 访问新浪官网首页(https://www.sina.com.cn/)
        2. 点击导航栏的“时尚”菜单
        3. 列出“最新”板块中前十条新闻的标题和发布时间,用json格式返回结果, 示范格式如下：[ { title: '时尚板块最新新闻标题1', publish_time: '3月3日 13:20'}]
        """,
        llm=llm,
        use_vision=False # 禁用视觉模式，依赖DOM解析
    )
    # 执行任务后输出结果    
    result = await agent.run()
    print("\n========测试结果=========")
    print(result.final_result())

asyncio.run(main())

