# AGENTS.md

## RodSki 用例任务（常驻）

涉及 `case/*.xml`、`model/*.xml`、`data/globalvalue.xml`、`data/data.sqlite`、`plan/*.xml` 或 RodSki 用例生成/审查时，动手前必须先读取 `TEST_CASE_WRITING_GUIDE.md` （注意迭代更新的内容模块）和目标模块现有文件风格。

- RodSki CLI 优先使用 `D:\Documents\pythonProject\venv\Scripts\rodski.exe`，先执行 `--version` 确认版本。
- 始终保持“关键字 + 模型 + 数据”三元结构：Case 只编排动作，Model 定义元素/接口字段，数据进入 `data/data.sqlite`，全局变量只放 `data/globalvalue.xml`。
- 禁止生成 `open`、`http_get`、`http_post`、`assert_json`、`assert_status` 等旧式/伪关键字；导航用 `navigate`，接口用 `send` + `verify`。
- UI 原子操作（如 click、hover、select、key_press、drag、scroll）不要写成 `test_step@action`，应写入数据行并由 `type` 批量执行。
- 完成前运行最小有效校验：`rodski data validate <module>` 与 `rodski run <case-or-case-dir> --dry-run --output-format json`；若本机存在 `/Users/zella/.codex/skills/rodski-case-writer/scripts/rodski_case_guard.py`，先用它扫描改动模块。

## Karpathy 编码准则（常驻）

所有代码任务默认遵守这四条，除非用户明确要求相反做法。

### 1. 先想再写
- 开始前把目标、约束、成功标准说清楚。
- 需求有多种合理解读时，先列出选项；低风险时说明选择，高风险时必须问。
- 需求不明确时，先列出假设；关键假设不能冒险猜，必须问。
- 有更简单或更稳妥的方案时直接指出，并说明取舍。

### 2. 极简优先
- 只实现当前请求需要的行为，不加顺手功能、未来扩展或过早抽象。
- 优先使用现有模式、现有工具和本地约定。
- 能用更少代码清楚解决时，主动收敛实现。
- 不为没有实际路径的假想场景增加复杂防御。

### 3. 外科手术式改动
- 只改完成任务所必需的文件和代码。
- 不顺手重构、格式化、美化或清理无关内容。
- 匹配既有风格；遇到无关问题可以指出，但不要擅自改。
- 清理自己改动造成的死代码、重复代码和临时产物。

### 4. 目标驱动验证
- 把任务转成可验证结果，再执行。
- 修 bug 先复现；加功能要覆盖关键路径；重构要证明行为不变。
- 多步任务要有简短计划，并在关键步骤对应验证方式。
- 完成前运行最小但有意义的检查，并说明验证结果。
