# RodSki 阅读理解笔记

> 阅读对象：<https://github.com/Sirius1942/RodSki>  
> 整理时间：2026-05-09  
> 目的：记录 RodSki 项目定位、核心结构、用例编写约束和后续在 `AICASS/improve` 中处理 RodSki 资产时应遵守的规则。

## 1. 项目定位

RodSki 是一个面向 AI Agent 的确定性自动化测试执行引擎。

它的核心分工是：

```text
AI Agent 负责：探索系统、理解需求、生成/修复测试资产、分析执行结果
RodSki 负责：按 XML/SQLite 测试资产稳定执行测试，并输出结构化结果
```

可以把它理解为：

```text
Agent -> XML / SQLite 测试资产 -> RodSki 执行 -> JSON/XML 结果 -> Agent 分析修复
```

RodSki 本身不是一个通用 Agent 框架，而是给 Agent 使用的测试执行层。它强调：

- 可审计：测试行为落在明确的 XML、模型和数据文件中。
- 可重复：同一份用例和数据应产生稳定执行过程。
- 可维护：Case、Model、Data 各自承担不同职责。
- 跨平台：覆盖 Web、Android、iOS、桌面端、接口、数据库、脚本等场景。

## 2. 核心三元结构

RodSki 用例资产的核心是：

```text
Case = 关键字编排，描述做什么
Model = 模型定义，描述操作哪个元素或接口字段
Data = 数据承载，描述输入值、期望值、SQL、变量
```

这三者必须保持边界清晰。

### Case

Case 通常位于：

```text
case/*.xml
```

Case 只负责动作流程，例如登录、导航、点击、输入、发送请求、验证结果等。Case 不应硬编码大量业务数据。

典型职责：

- 编排测试步骤。
- 调用关键字。
- 通过 `data` 引用数据行。
- 串联不同模型和页面动作。

### Model

Model 通常位于：

```text
model/model.xml
```

Model 定义被操作对象，例如：

- Web 页面元素。
- App 页面元素。
- 接口请求字段。
- 接口响应验证字段。
- 数据库或其他可执行对象的结构映射。

Model 的重点是把“怎么定位/怎么识别对象”从 Case 中抽离出来。

### Data

Data 主要位于：

```text
data/data.sqlite
data/globalvalue.xml
```

其中：

- `data/data.sqlite` 是业务测试数据的主要承载位置。
- `data/globalvalue.xml` 只放全局变量、环境变量、公共配置类值。

后续新增或修改用例时，应优先把输入值、期望值、SQL、接口参数、UI 操作参数放进 SQLite 数据表，而不是写死在 Case 文件中。

## 3. 推荐模块目录结构

一个标准 RodSki 模块大致应保持如下结构：

```text
module/
  case/
    *.xml
  model/
    model.xml
  fun/
    ...
  data/
    globalvalue.xml
    data.sqlite
  plan/
    *.xml
  result/
    ...
```

各目录职责：

| 目录 | 职责 |
| --- | --- |
| `case/` | 测试用例 XML，编排测试步骤 |
| `model/` | 模型 XML，定义元素、字段、定位器 |
| `fun/` | 可复用流程或函数 |
| `data/` | SQLite 数据、全局变量 |
| `plan/` | 测试计划 |
| `result/` | 执行结果 |

## 4. 关键命名关系

RodSki 的模型和数据强依赖命名一致性。

### Model 名称与数据表名称

模型名应与逻辑数据表名保持一致。例如：

```text
Model: login
Data table: login
```

### Model 字段与数据字段

模型元素的 `name` 应与数据字段 `name` 保持一致。例如：

```xml
<element name="username" ... />
```

对应数据表中也应有：

```text
username
```

### Case 中的 data 引用

Case 中的 `data` 应优先引用 DataID，而不是直接写业务值。例如：

```xml
<test_step action="type" model="login" data="L001" />
```

这里的 `L001` 指向数据表中的一行数据。

## 5. 关键字使用原则

### UI 操作

UI 操作应优先通过 `type` 批量执行数据行中声明的动作。

常见 UI 原子动作包括：

- `click`
- `hover`
- `select`
- `key_press`
- `drag`
- `scroll`

这些动作不应优先写成大量单独的 `test_step@action`。更推荐的方式是：

```text
Case 中执行 type
Data 行中声明每个字段对应的动作类型、输入值或操作参数
Model 中声明每个字段的定位方式
```

这样可以保持：

- Case 简洁。
- Model 稳定。
- Data 可批量维护。

### 页面导航

页面导航使用：

```text
navigate
```

不应生成旧式或伪造的 `open` 关键字。

### 接口测试

接口测试使用：

```text
send + verify
```

其中：

- `send` 发送请求。
- `verify` 校验响应。

不应生成旧式或伪关键字，例如：

```text
http_get
http_post
assert_json
assert_status
```

### verify 默认数据表

`verify` 默认查找：

```text
{model}_verify
```

例如模型为：

```text
order
```

则验证数据表通常是：

```text
order_verify
```

## 6. 数据层规则

### SQLite 是主要数据源

业务数据、接口参数、验证期望、UI 操作参数等，应进入：

```text
data/data.sqlite
```

适合放入 SQLite 的内容：

- 登录账号。
- 表单输入值。
- 查询条件。
- 接口请求体字段。
- 接口响应期望。
- 数据库 SQL。
- UI 动作参数。

### globalvalue.xml 只放全局值

`globalvalue.xml` 适合放：

- 环境地址。
- 全局 token。
- 公共账号配置。
- 公共路径。
- 运行时公共变量。

不应把模块级、场景级、用例级的大量业务测试数据塞进 `globalvalue.xml`。

## 7. CLI 与安装理解

RodSki 的命令行入口来自 `pyproject.toml`：

```text
rodski = "rodski.cli_main:main"
```

基础开发安装方式：

```bash
pip install -e .
```

Web 自动化能力通常需要：

```bash
pip install -e ".[web]"
playwright install
```

项目还按能力划分了可选依赖，例如：

- Web。
- Mobile。
- GUI。
- Visual。
- LLM。
- Dev/Test。

后续在本工作区使用时，应优先确认本机实际可用的 RodSki CLI。

当前 `AICASS/improve/AGENTS.md` 中记录的历史路径是 macOS 路径：

```text
/Users/zella/TestCase/myenv/bin/rodski
```

但当前环境是 Windows：

```text
D:\Documents\pythonProject
```

因此本机实际运行时，应以当前工作区可用命令为准，例如先检查：

```powershell
venv\Scripts\rodski.exe --version
```

或根据实际安装位置执行：

```powershell
rodski --version
```

## 8. 最小验证流程

修改 RodSki 用例资产后，应尽量执行最小但有效的验证。

推荐顺序：

```bash
rodski data validate <module>
rodski run <case-or-case-dir> --dry-run --output-format json
```

其中：

- `data validate` 用于检查数据、模型和引用关系。
- `dry-run` 用于验证用例结构、关键字、数据引用和执行计划是否合理。
- `--output-format json` 便于 Agent 读取并分析失败原因。

如果本地存在额外守护脚本，也应先使用。例如 `AGENTS.md` 提到：

```text
/Users/zella/.codex/skills/rodski-case-writer/scripts/rodski_case_guard.py
```

但该路径是 macOS 风格，当前 Windows 环境下需要先确认是否存在等效脚本。

## 9. 在 AICASS/improve 中的工作约束

后续涉及以下文件时，应先阅读本笔记和目标模块现有资产：

```text
case/*.xml
model/*.xml
data/globalvalue.xml
data/data.sqlite
plan/*.xml
```

具体规则：

1. 先理解目标模块现有风格，不直接套模板。
2. 保持 Case、Model、Data 三层职责分离。
3. 不把测试数据硬编码进 Case。
4. 不把页面元素定位器硬编码进 Case。
5. 不生成旧式关键字或伪关键字。
6. UI 原子动作优先进入数据行，由 `type` 批量执行。
7. 接口用例使用 `send + verify`。
8. 导航使用 `navigate`。
9. 验证数据表按 `{model}_verify` 约定组织。
10. 修改完成后执行最小验证；若因环境限制无法执行，应说明原因。

## 10. 快速检查清单

处理 RodSki 资产前：

- [ ] 是否已阅读目标模块现有 `case/`、`model/`、`data/`？
- [ ] 是否确认模型名和数据表名一致？
- [ ] 是否确认模型字段名和数据字段名一致？
- [ ] 是否避免在 Case 中硬编码业务数据？
- [ ] 是否避免在 Case 中硬编码定位器？
- [ ] 是否使用 `navigate` 而不是 `open`？
- [ ] 是否使用 `send + verify` 而不是旧式接口关键字？
- [ ] UI 原子动作是否优先放入数据表？
- [ ] 是否准备好执行 `data validate`？
- [ ] 是否准备好执行 `dry-run`？

## 11. 参考链接

- RodSki 仓库：<https://github.com/Sirius1942/RodSki>
- Agent 集成指南：<https://github.com/Sirius1942/RodSki/blob/main/rodski/docs/AGENT_INTEGRATION.md>
- 用例编写指南：<https://github.com/Sirius1942/RodSki/blob/main/rodski/docs/TEST_CASE_WRITING_GUIDE.md>
- 关键字参考：<https://github.com/Sirius1942/RodSki/blob/main/rodski/docs/SKILL_REFERENCE.md>
- 打包配置：<https://github.com/Sirius1942/RodSki/blob/main/pyproject.toml>
