#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File: overseas.py
@ Time: 2025/3/21 17:10
@ Author: lululi
@ version: python 3.13
@ Description: 1、连接AI
"""


from quart import Quart, jsonify, request
from langchain_openai import ChatOpenAI
from browser_use import Agent
import os
import json
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Quart(__name__)

# 全局初始化模型
llm = ChatOpenAI(
    base_url='http://116.63.86.12:3000/v1',
    model='Doubao-DeepSeek-V3',
    # model='fc-llm',
    api_key=os.environ.get('DEEPSEEK_API_KEY')
)


# 创建 Agent 并定义任务
def create_agent(task):
    return Agent(
        task=task,
        llm=llm,
        use_vision=False  # 禁用视觉模式，依赖 DOM 解析
    )


# 异步执行任务
async def run_task(task):
    agent = create_agent(task)  # 创建 agent
    result = await agent.run()  # 执行任务
    return json.loads(result.final_result())  # 返回结果


# 定义 API 路由，接收 POST 请求并传递 task
@app.route('/run-task', methods=['POST'])
async def run_task_endpoint():
    try:
        # 获取请求中的 JSON 数据
        data = await request.get_json()
        task = data.get('task')  # 获取 'task' 字段

        if not task:
            return jsonify({'error': 'Task is required'}), 400

        # 使用异步方式执行任务
        result = await run_task(task)

        return jsonify(result)  # 返回结果
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 启动 Quart 应用
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

    