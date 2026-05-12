# RodSki 阅读理解笔记

> 阅读对象：<https://github.com/Sirius1942/RodSki>  
> 重点补充来源：`AICASS/docs/TEST_CASE_WRITING_GUIDE.md`（RodSki v6.3，2026-05-07）  
> 整理时间：2026-05-12  
> 目的：记录 RodSki 项目定位、核心结构、用例编写约束和后续在 `AICASS` 中处理 RodSki 资产时应遵守的规则。

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
用例 = 关键字（做什么动作） + 模型（对哪些元素/字段） + 数据（用什么值）
```

也可以拆成：

```text
Case = 关键字编排，描述做什么
Model = 模型定义，描述操作哪个元素、接口字段或数据库对象
Data = 数据承载，描述输入值、期望值、SQL、变量
```

最重要的基础规则是：

```text
模型元素 name = 数据表字段 name
模型名 = data.sqlite 中的逻辑表名
verify 默认读取 {模型名}_verify 逻辑表
```

这三层必须保持边界清晰：

- Case 只编排流程，不硬编码大量业务数据，不硬编码定位器。
- Model 管定位和字段映射，不承载测试数据。
- Data 承载输入值、期望值、接口参数、SQL、UI 动作参数等。

## 3. 标准模块目录结构

RodSki v3.0+ 使用固定目录结构组织测试模块。一个标准模块应保持如下结构：

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
| `model/` | 模型 XML，定义元素、字段、定位器、接口字段、数据库对象 |
| `fun/` | `run` 关键字调用的脚本工程 |
| `data/` | `data.sqlite` 测试数据与 `globalvalue.xml` 全局变量 |
| `plan/` | 测试计划 XML |
| `result/` | 框架自动生成的执行结果 |

`data/data.sqlite` 是唯一运行时测试数据文件。历史 XML 数据表只用于迁移，不再作为运行时数据源。

## 4. Case XML 编写硬约束

### 4.1 根结构

Case 文件根元素为 `<cases>`，每个 `<case>` 下使用三阶段容器：

```xml
<cases tags="smoke,login" step_wait="500">
  <case execute="是" id="TC001" title="登录测试" component_type="界面" priority="P0">
    <pre_process>
      <test_step action="navigate" model="" data="GlobalValue.DefaultValue.URL/login"/>
    </pre_process>
    <test_case>
      <test_step action="type" model="Login" data="L001"/>
      <test_step action="verify" model="Login" data="V001"/>
    </test_case>
    <post_process>
      <test_step action="close" model="" data=""/>
    </post_process>
  </case>
</cases>
```

硬约束：

- 每个 `<case>` 必须且仅有 1 个 `<test_case>`。
- `<test_case>` 内至少 1 个执行项；执行项可以是裸 `<test_step>`，v6.3.0 起也可以是 `<scenario>`。
- `<pre_process>` 和 `<post_process>` 可选，各最多 1 个，内部可有 0 到多个 `<test_step>`。
- 执行顺序固定为 `pre_process -> test_case -> post_process`。
- 预处理失败时跳过用例主体，但仍执行后处理。
- 用例主体失败时仍执行后处理。
- 后处理失败时整条用例失败。

### 4.2 `<cases>` 与 `<case>` 属性

`<cases>` 常用属性：

| 属性 | 说明 |
| --- | --- |
| `step_wait` | 步骤间等待时间，单位毫秒；覆盖 GlobalValue 中的 WaitTime |
| `tags` | 套件标签，逗号分隔，文件内用例共享 |

`<case>` 常用属性：

| 属性 | 约束 |
| --- | --- |
| `execute` | 必填；只能是 `是` 或 `否` |
| `id` | 必填；用于日志、结果和 plan 引用 |
| `title` | 必填；用于日志和报告 |
| `description` | 可选 |
| `component_type` | 可选；只能是 `界面`、`接口`、`数据库` |
| `priority` | 可选；建议使用 `P0`、`P1`、`P2`、`P3` |
| `expect_fail` | 可选；`是` / `否`，预期失败用例失败时不计入 FAIL |

### 4.3 `test_step` 属性

`test_step` 是执行动作的最小静态单元：

| 属性 | 约束 |
| --- | --- |
| `action` | 必填；必须是 `case.xsd` 的 `ActionType` 枚举值，大小写敏感 |
| `model` | 可选；`type` / `verify` / `send` / `DB` 等需要模型名，`navigate` / `close` / `wait` 等可留空 |
| `data` | 可选；通常为 DataID，也可以是 GlobalValue 引用、URL、秒数等关键字参数 |

Case 中 `data` 对核心批量关键字只写 DataID，不写表名前缀。例如：

```xml
<!-- 正确 -->
<test_step action="send" model="RegisterAPI" data="L001"/>

<!-- 错误：data 不写 RegisterAPI.L001 -->
<test_step action="send" model="RegisterAPI" data="RegisterAPI.L001"/>
```

### 4.4 scenario 容器

v6.3.0 起，`<test_case>` 内可使用 `<scenario>` 对步骤分组：

```xml
<test_case>
  <test_step action="type" model="LoginForm" data="L001"/>

  <scenario id="S001" title="进入功能页" group="smoke" tag="nav,ui">
    <test_step action="type" model="NavMenu" data="N001"/>
  </scenario>

  <scenario id="S002" title="提交表单" group="smoke" tag="form" depends="S001">
    <test_step action="type" model="Form" data="D001"/>
    <test_step action="verify" model="Form" data="V001"/>
  </scenario>
</test_case>
```

规则：

- `scenario` 只在当前 `<test_case>` 内分组，不替代 `<case>`。
- `id` 必填，并且在同一 case 内唯一。
- `title`、`group`、`tag`、`depends` 可选。
- 裸 `test_step` 与 `scenario` 按书写顺序混合执行。
- `depends` 只判断同一 case 内已执行过的 scenario；依赖失败或跳过时，当前 scenario 标记为 `SKIP`。
- scenario 失败会导致 case 失败；后处理仍执行。

## 5. 合法 action 与关键字使用原则

`action` 必须与 `case.xsd` 的 `ActionType` 枚举一致。常用合法值包括：

```text
close
type
verify
wait
navigate
assert
upload_file
clear
get_text
get
evaluate
send
set
DB
run
check
screenshot
```

注意：

- `get_text` 已废弃，应改用 `get`。
- `check` 与 `verify` 等价，主要用于兼容。
- `evaluate` 仅 Web 场景使用，优先级较低。
- 不应生成 `open`、`http_get`、`http_post`、`assert_json`、`assert_status` 等旧式或伪关键字。

### UI 操作

UI 主链路优先使用 `type` 批量执行：

```xml
<test_step action="type" model="Login" data="L001"/>
```

`click`、`select`、`hover`、`scroll`、`double_click`、`right_click`、`key_press`、`drag` 等 UI 原子动作不是独立 action，而是写在数据表 field 值中，由 `type` 批量模式识别。

### 页面导航

页面导航使用：

```xml
<test_step action="navigate" model="" data="GlobalValue.DefaultValue.URL"/>
```

### 接口测试

接口测试使用：

```xml
<test_step action="send" model="LoginAPI" data="D001"/>
<test_step action="verify" model="LoginAPI" data="V001"/>
```

接口模型元素约定：

| 元素名 | 作用 |
| --- | --- |
| `_method` | HTTP 请求方法，如 GET / POST / PUT / DELETE |
| `_url` | 请求地址，绝对 URL 或相对路径 |
| `_header_*` | 请求头，如 `_header_Authorization` |
| 其他元素 | 请求体字段或查询参数 |

### 数据库测试

DB 用例使用：

```xml
<test_step action="DB" model="QuerySQL" data="Q001"/>
```

规则：

- `model` 填数据库模型名，不填 GlobalValue 连接组名。
- 数据库模型必须是 `type="database"`。
- 数据库模型通过 `connection="sqlite_db"` 指向 `globalvalue.xml` 中的连接组。
- 数据行可通过 `query` 字段引用模型内定义的 query，也可以通过 `sql` 字段直接提供 SQL。

## 6. model.xml 编写规则

模型文件根元素为 `<models>`，常见结构：

```xml
<models>
  <model name="Login" servicename="">
    <element name="username" type="web">
      <type>input</type>
      <location type="id">username</location>
      <desc>用户名输入框</desc>
    </element>
  </model>
</models>
```

硬约束：

- `<model>` 必须有 `name`。
- `<element>` 必须有 `name`。
- `<element name>` 必须与数据表字段名完全一致，区分大小写。
- 定位器必须使用 `<location type="...">值</location>` 子节点格式。
- 已废弃的简化属性格式 `type="定位类型" value="值"` 不再使用。

传统定位器包括：

```text
id
class
css
xpath
text
tag
name
static
field
```

视觉定位器包括：

```text
vision
ocr
vision_bbox
```

多定位器可通过多个 `<location>` 并设置 `priority` 实现失败自动切换。

## 7. 数据层规则

### 7.1 SQLite 是唯一运行时数据源

所有测试数据统一存储在：

```text
data/data.sqlite
```

SQLite 使用 EAV 元表结构：

| 元表 | 说明 |
| --- | --- |
| `rs_datatable` | 逻辑表注册，`table_name` 等于模型名 |
| `rs_datatable_field` | 字段 schema |
| `rs_row` | 数据行，使用 `data_id` |
| `rs_field` | 字段值 |

约束：

- 输入逻辑表名必须与模型名一致。
- 验证数据表名为 `{模型名}_verify`，`table_kind='verify'`。
- 输入数据表 `table_kind='data'`。
- 同一逻辑表所有行的字段集合必须完全一致，并与 schema 一致。
- Case 的 `data` 对批量关键字只写 DataID，由 `model` 自动推导逻辑表。

### 7.2 数据表命名与引用

| 关键字 | Case 写法 | 自动推导逻辑表 |
| --- | --- | --- |
| `type` | `model="Login" data="L001"` | `Login` |
| `verify` | `model="Login" data="V001"` | `Login_verify` |
| `send` | `model="LoginAPI" data="D001"` | `LoginAPI` |
| `DB` | `model="QuerySQL" data="Q001"` | `QuerySQL` |

适合放入 SQLite 的内容：

- 登录账号。
- 表单输入值。
- 查询条件。
- 接口请求体字段。
- 接口响应期望。
- 数据库 SQL。
- UI 动作参数。

### 7.3 批量输入中的特殊值

数据表字段值有特殊语义：

| 值 | 语义 |
| --- | --- |
| `.Password` 后缀 | 输入时去掉后缀，日志脱敏显示 `***` |
| 省略 field | UI 中跳过该元素 |
| `BLANK` | UI 跳过或接口传空字符串，按场景处理 |
| `NULL` / `NONE` | UI 跳过，接口传 null / none |

UI 动作值写在 field 中：

| 动作值 | 示例 |
| --- | --- |
| `click` | `<field name="loginBtn">click</field>` |
| `double_click` | `<field name="item">double_click</field>` |
| `right_click` | `<field name="menu">right_click</field>` |
| `hover` | `<field name="tooltip">hover</field>` |
| `select【管理员】` | `<field name="role">select【管理员】</field>` |
| `key_press【Tab】` | `<field name="password">key_press【Tab】</field>` |
| `key_press【Control+C】` | `<field name="input">key_press【Control+C】</field>` |
| `drag【#drop-zone】` | `<field name="card">drag【#drop-zone】</field>` |
| `scroll` | 默认向下滚动 |
| `scroll【0,500】` | 自定义滚动距离 |

动作参数使用中文方括号 `【】` 包裹。

## 8. GlobalValue 与变量解析

`globalvalue.xml` 固定放在 `data/` 目录：

```xml
<globalvalue>
  <group name="DefaultValue">
    <var name="URL" value="http://127.0.0.1:5555"/>
    <var name="BrowserType" value="chromium"/>
    <var name="WaitTime" value="2"/>
  </group>
</globalvalue>
```

约束：

- 全文件内 `<group name>` 不得重名。
- 同一 group 内 `<var name>` 不得重名。
- 每个 `<var>` 必须同时有 `name` 和 `value`。
- 引用语法为 `GlobalValue.组名.变量名`。

适合放入 `globalvalue.xml` 的内容：

- 环境地址。
- 浏览器类型。
- 默认等待时间。
- 全局 token。
- 公共账号配置。
- 公共路径。
- 数据库连接配置。

不应把模块级、场景级、用例级的大量业务测试数据塞进 `globalvalue.xml`。

`DefaultValue.WaitTime` 表示每个步骤执行完成后的自动等待秒数。`navigate`、`type`、`verify` 等应用 WaitTime；`wait` 本身不再叠加；`close` 不应用。

## 9. Return、set/get 与数据引用

框架执行前对 `data` 或字段值的解析顺序为：

```text
GlobalValue 引用 -> 数据表字段引用 -> Return 引用
```

支持的引用格式：

| 格式 | 说明 |
| --- | --- |
| `GlobalValue.组名.Key` | 全局变量 |
| `表名.DataID` | 整行数据 |
| `表名.DataID.字段名` | 单字段值 |
| `${Return[-1]}` | 上一步返回值，应写在数据表 field 中 |
| `${Return[-2]}` | 上上步返回值，应写在数据表 field 中 |
| `${Return[0]}` | 第一步返回值，应写在数据表 field 中 |

Return 使用规则：

- Return 引用应写在数据表 field 值中，不应直接写在 Case XML 的 `data` 属性。
- 接口和数据库模型的 `_verify` 表禁止使用 `${Return[-1]}` 做期望值，因为 verify 会自动从上一步 Return 读取实际值，自引用会让断言失效。
- UI verify 可使用 `${Return[-N]}` 做跨源比对。
- 若未来支持运行时插入动态步骤，`${Return[-1]}` 仍表示固定步骤链路上的上一步，不应用来引用动态步骤结果。

会产生 Return 的关键字：

| 关键字 | 返回内容 |
| --- | --- |
| `get` / `get_text` | 元素文本；`get_text` 已废弃 |
| `verify` | 批量验证实际值字典 |
| `assert` | 断言结果 |
| `type` | 本次输入使用的数据行 |
| `send` | HTTP 响应，含 `status` 和响应体字段 |
| `DB` | query 返回结果集，execute 返回受影响行数 |
| `run` | 脚本 stdout，框架自动尝试 JSON 解析 |

推荐优先使用 `set` / `get` 命名变量传递跨步骤数据，减少 `${Return[-N]}` 索引偏移风险。

## 10. plan 与执行范围

v6.3.0 起，RodSki 支持 `plan/*.xml` 定义本次执行范围，控制 case、scenario、step。

两种执行范围来源：

| 模式 | 示例 | 说明 |
| --- | --- | --- |
| 显式 plan | `rodski run @invoice_smoke` | 执行范围来自 `plan/*.xml` |
| 临时 selector | `rodski run --tag smoke` | 执行范围来自 case/scenario 元数据 |

显式 plan 与临时 selector 不能在同一次 `rodski run` 中组合。例如以下写法应避免：

```bash
rodski run @invoice_smoke --tag smoke
rodski run @invoice_smoke --group negative
rodski run @invoice_smoke --exclude-tag slow
rodski run @invoice_smoke --priority P0
```

如果需要长期保存 tag 筛选结果，应先生成 plan，再执行 plan。

执行关闭优先级：

```text
case XML 中 <case execute="否">（最高，硬关闭）
  > test_plan.execute="否"
  > plan case execute="否"
  > plan scenario execute="否"
  > plan step execute="否"
  > test_plan.default_execute（最低）
```

只要上层关闭，下层即使显式开启也不会执行。

## 11. run 脚本规则

`run` 在独立子进程中执行 `fun/` 下的 Python 脚本，stdout 自动保存为步骤返回值。

目录组织：

```text
module/
  fun/
    data_gen/
      gen_phone.py
    crypto/
      encrypt.py
```

Case 写法：

```xml
<test_step action="run" model="data_gen" data="gen_phone.py"/>
```

脚本通过 `print()` 输出返回值，框架会自动尝试 JSON 解析。

桌面端特有操作，例如剪贴板、组合键、窗口切换，也应通过 `run` 调用脚本实现，不新增 `clipboard`、`key_combination`、`window` 等独立关键字。

## 12. 视觉定位器与桌面端

视觉定位器通过 OmniParser 服务和多模态 LLM 实现语义定位，适用于传统 xpath/css 不稳定或元素无明显属性的场景。

常用写法：

```xml
<element name="loginBtn" type="web">
  <location type="vision">登录按钮</location>
</element>

<element name="submitBtn" type="web">
  <location type="vision_bbox">100,200,150,250</location>
</element>
```

约束：

- Web 中 `vision_bbox` 使用页面像素坐标。
- Desktop 中 `vision_bbox` 使用屏幕绝对坐标。
- 传统 Web 元素仍优先使用 xpath/css/id 等更快、更稳定的定位器。
- 桌面平台通过模型上的 `driver_type="windows"` 或 `driver_type="macos"` 标识。
- 桌面端不支持接口测试，不使用 `send`。
- 桌面操作以视觉定位为主，辅以 `run` 调用脚本。

指南中出现 `launch` 桌面启动示例，但当前 action 枚举清单未列出 `launch`。编写用例时应以实际 `case.xsd` 与当前 RodSki 版本支持的 action 为准；若本地 XSD 未支持，不应直接生成 `launch`。

## 13. CLI 与安装理解

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

项目按能力划分了可选依赖，例如 Web、Mobile、GUI、Visual、LLM、Dev/Test。

当前环境是 Windows：

```text
D:\Documents\pythonProject
```

本机实际运行时，应以当前工作区可用命令为准，例如先检查：

```powershell
venv\Scripts\rodski.exe --version
```

或根据实际安装位置执行：

```powershell
rodski --version
```

## 14. 最小验证流程

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

常用数据命令：

```bash
rodski data list <module>
rodski data schema <module> <table>
rodski data show <module> <table> <data_id>
rodski data query <module> <table> --limit 20
rodski data validate <module>
rodski data import <module> [--overwrite]
```

如本地存在额外守护脚本，也应先确认路径并使用。历史 macOS 路径不能直接套用到当前 Windows 工作区。

## 15. 在 AICASS 中处理 RodSki 资产的工作约束

后续涉及以下文件时，应先阅读本笔记、用例编写指南和目标模块现有资产：

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
6. `action` 必须来自当前 `case.xsd` 枚举。
7. 每个 case 必须有且仅有一个 `<test_case>`。
8. `execute` 只能写 `是` 或 `否`。
9. `component_type` 只能写 `界面`、`接口`、`数据库`。
10. UI 原子动作优先进入数据行，由 `type` 批量执行。
11. 接口用例使用 `send + verify`。
12. 导航使用 `navigate`。
13. 验证数据表按 `{model}_verify` 约定组织。
14. Case 中核心批量关键字的 `data` 只写 DataID，不写 `表名.DataID`。
15. Return 引用写入数据表 field，不直接写 Case `data`。
16. 接口/DB 的 `_verify` 表不使用 `${Return[-1]}` 自引用。
17. DB 的 `model` 填数据库模型名，连接组由模型映射到 `globalvalue.xml`。
18. 修改完成后执行最小验证；若因环境限制无法执行，应说明原因。

## 16. 快速检查清单

处理 RodSki 资产前：

- [ ] 是否已阅读目标模块现有 `case/`、`model/`、`data/`？
- [ ] 是否确认每个 `<case>` 有且仅有一个 `<test_case>`？
- [ ] 是否确认 `execute` 只使用 `是` / `否`？
- [ ] 是否确认 `component_type` 只使用 `界面` / `接口` / `数据库`？
- [ ] 是否确认 `action` 在当前 `case.xsd` 枚举内？
- [ ] 是否确认模型名和数据逻辑表名一致？
- [ ] 是否确认模型元素名和数据字段名一致？
- [ ] 是否避免在 Case 中硬编码业务数据？
- [ ] 是否避免在 Case 中硬编码定位器？
- [ ] 是否使用 `navigate` 而不是 `open`？
- [ ] 是否使用 `send + verify` 而不是旧式接口关键字？
- [ ] UI 原子动作是否优先放入数据表 field？
- [ ] verify 数据表是否使用 `{model}_verify`？
- [ ] Case 中批量关键字 `data` 是否只写 DataID？
- [ ] Return 引用是否只写在数据表 field 中？
- [ ] 接口/DB `_verify` 表是否避免 `${Return[-1]}` 自引用？
- [ ] 是否准备好执行 `rodski data validate <module>`？
- [ ] 是否准备好执行 `rodski run <case-or-case-dir> --dry-run --output-format json`？

## 17. 参考链接

- RodSki 仓库：<https://github.com/Sirius1942/RodSki>
- Agent 集成指南：<https://github.com/Sirius1942/RodSki/blob/main/rodski/docs/AGENT_INTEGRATION.md>
- 用例编写指南：<https://github.com/Sirius1942/RodSki/blob/main/rodski/docs/TEST_CASE_WRITING_GUIDE.md>
- 关键字参考：<https://github.com/Sirius1942/RodSki/blob/main/rodski/docs/SKILL_REFERENCE.md>
- 打包配置：<https://github.com/Sirius1942/RodSki/blob/main/pyproject.toml>
