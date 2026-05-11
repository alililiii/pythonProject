# 维修厂发布询价自动化用例

## 用例目标

使用维修厂账号登录后，发布一条常规询价：

- 账号：`13119909586`
- 密码：`123456Aa`
- VIN：`LBVFR790XBSD31722`
- 配件名称：`火花塞`

## 文件说明

- `case/publish_inquiry.xml`：RodSki 流程编排。
- `model/model.xml`：页面元素定位，按规则使用子 `<location>` 写法。
- `data/globalvalue.xml`：环境入口地址。
- `data/data.sqlite`：登录、输入、验证数据。

## 编写依据

- 参考 `D:\Documents\pythonProject\AICASS\improve\PEER_QUOTE_FILLBACK_CASE_EXPERIENCE.md`。
- 登录链路采用 `navigate -> type -> wait -> verify`。
- 弹窗处理通过当前可见弹窗/可见元素范围判断。
- 发布成功通过详情页“询价单：”标签和 B 开头询价单号校验。
