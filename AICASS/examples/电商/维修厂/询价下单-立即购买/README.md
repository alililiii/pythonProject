# 维修厂发布询价自动化用例

## 用例目标

使用维修厂账号登录后，发布一条常规询价：

- 账号：`13119909586`
- 密码：`123456Aa`
- VIN：`LBVFR790XBSD31722`
- 配件名称：`火花塞`、`机油格`

## 文件说明

- `case/publish_inquiry.xml`：RodSki 流程编排，使用 v6.3+ `<scenario>` 拆分主链路。
- `model/model.xml`：页面元素定位，按规则使用子 `<location>` 写法。
- `data/globalvalue.xml`：环境入口地址。
- `data/data.sqlite`：登录、输入、验证数据。

## Scenario 拆分

用例主体保留单个 `<test_case>`，内部按 RodSki v6.3+ 的 `<scenario>` 组织主链路，并通过 `depends` 表达执行依赖。

| Scenario ID | 分组 | 标签 | 场景说明 |
| --- | --- | --- | --- |
| `GARAGE_PUBLISH_001_ASSERT_READY` | `garage_publish` | `inquiry,publish,p0,smoke,assert` | 确认维修厂发布询价页面可用。 |
| `GARAGE_PUBLISH_001_INPUT_INQUIRY` | `garage_publish` | `inquiry,publish,p0,smoke,input` | 录入 VIN 和两个配件名称；若出现“当前VIN码已在询价中”弹窗则点击“不追加，发布新询价单”。 |
| `GARAGE_PUBLISH_001_SUBMIT` | `garage_publish` | `inquiry,publish,p0,smoke,submit` | 等待发布按钮可用，提交询价，并处理发布阶段可能出现的“当前VIN码已在询价中”弹窗。 |
| `GARAGE_PUBLISH_001_ASSERT_SUCCESS` | `garage_publish` | `inquiry,publish,p0,smoke,assert` | 校验进入询价详情页、展示目标 VIN 和两个配件、生成 B 开头询价单号，并截图留存。 |

## 编写依据

- 参考 `D:\Documents\pythonProject\AICASS\improve\PEER_QUOTE_FILLBACK_CASE_EXPERIENCE.md`。
- 登录链路采用 `navigate -> type -> wait -> verify`。
- 弹窗处理通过当前可见弹窗/可见元素范围判断。
- 发布成功通过详情页“询价单：”标签和 B 开头询价单号校验。
