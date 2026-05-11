# 电商三端登录模块 RodSki 自动化用例

## 覆盖范围

本模块整合电商三端登录自动化，覆盖管理中心、维修厂和供应商：

- 管理中心 admin：`https://ec-hwbeta.casstime.com/admin#`
- 维修厂 mall：`https://ec-hwbeta.casstime.com/mall`
- 供应商 seller：`https://ec-hwbeta.casstime.com/seller`

## 目录结构

```text
AICASS/examples/电商/登录/
  case/login_cases.xml
  model/model.xml
  data/globalvalue.xml
  data/data.sqlite
  fun/
  result/
```

## 用例清单

| 用例ID | 优先级 | 默认执行 | 覆盖点 |
| --- | --- | --- | --- |
| `ADMIN_LOGIN_001` | P0 | 是 | 管理中心未登录访问 admin 应被认证拦截 |
| `ADMIN_LOGIN_002` | P0 | 是 | 管理中心账号登录 admin 后进入管理中心首页 |
| `ADMIN_LOGIN_003` | P0 | 是 | 管理中心账号登录 admin 后退出登录 |
| `MALL_LOGIN_001` | P0 | 是 | 维修厂账号登录 mall 后进入维修厂商城 |
| `MALL_LOGIN_002` | P0 | 是 | 维修厂账号登录 mall 后退出登录 |
| `SELLER_LOGIN_001` | P0 | 是 | 供应商账号登录 seller 后进入供应商中心 |
| `SELLER_LOGIN_002` | P0 | 是 | 供应商账号登录 seller 后退出登录 |

## 测试账号

| 角色 | 账号 | 密码 |
| --- | --- | --- |
| 管理中心 | `mandy` | `Init@1125!@#$` |
| 维修厂 | `13119909586` | `123456Aa` |
| 供应商 | `ksseller1` | `Init@1125` |

账号数据同时保存在 `data/globalvalue.xml` 和 `data/data.sqlite` 中，RodSki 执行时以 `data.sqlite` 的 `PassportLogin` 数据表为准。

## Scenario 拆分

用例主体使用 RodSki v6.3+ 的 `<scenario>` 结构，按“打开入口 / 提交登录 / 结果断言 / 退出断言”拆分，并通过 `depends` 表达主链路依赖。

| 用例ID | Scenario ID | 分组 | 标签 | 场景说明 |
| --- | --- | --- | --- | --- |
| `ADMIN_LOGIN_001` | `ADMIN_LOGIN_001_ACCESS_ADMIN` | `admin` | `login,admin,p0,smoke,unauthenticated` | 未登录访问管理中心 admin 首页 |
| `ADMIN_LOGIN_001` | `ADMIN_LOGIN_001_ASSERT_BLOCKED` | `admin` | `login,admin,p0,smoke,assert` | 校验管理中心未登录访问被认证拦截 |
| `ADMIN_LOGIN_002` | `ADMIN_LOGIN_002_OPEN_LOGIN` | `admin` | `login,admin,p0,smoke,navigate` | 打开管理中心 admin 登录入口 |
| `ADMIN_LOGIN_002` | `ADMIN_LOGIN_002_SUBMIT_VALID` | `admin` | `login,admin,p0,smoke,submit` | 使用管理中心有效账号提交登录 |
| `ADMIN_LOGIN_002` | `ADMIN_LOGIN_002_ASSERT_HOME` | `admin` | `login,admin,p0,smoke,assert` | 校验进入管理中心 admin 首页 |
| `ADMIN_LOGIN_003` | `ADMIN_LOGIN_003_LOGIN_FIRST` | `admin_logout` | `login,admin,p0,smoke,prepare` | 先登录进入管理中心 admin 首页 |
| `ADMIN_LOGIN_003` | `ADMIN_LOGIN_003_LOGOUT` | `admin_logout` | `login,admin,p0,smoke,logout` | 执行管理中心 admin 退出登录 |
| `ADMIN_LOGIN_003` | `ADMIN_LOGIN_003_ASSERT_LOGOUT` | `admin_logout` | `login,admin,p0,smoke,assert` | 校验管理中心 admin 退出后离开已登录状态 |
| `MALL_LOGIN_001` | `MALL_LOGIN_001_OPEN_LOGIN` | `mall` | `login,mall,p0,smoke,navigate` | 打开维修厂 mall 登录入口 |
| `MALL_LOGIN_001` | `MALL_LOGIN_001_SUBMIT_VALID` | `mall` | `login,mall,p0,smoke,submit` | 使用维修厂有效账号提交登录 |
| `MALL_LOGIN_001` | `MALL_LOGIN_001_ASSERT_HOME` | `mall` | `login,mall,p0,smoke,assert` | 校验进入维修厂 mall 已登录页面 |
| `MALL_LOGIN_002` | `MALL_LOGIN_002_LOGIN_FIRST` | `mall_logout` | `login,mall,p0,smoke,prepare` | 先登录进入维修厂 mall |
| `MALL_LOGIN_002` | `MALL_LOGIN_002_LOGOUT` | `mall_logout` | `login,mall,p0,smoke,logout` | 执行维修厂 mall 退出登录 |
| `MALL_LOGIN_002` | `MALL_LOGIN_002_ASSERT_LOGOUT` | `mall_logout` | `login,mall,p0,smoke,assert` | 校验维修厂 mall 退出后离开已登录状态 |
| `SELLER_LOGIN_001` | `SELLER_LOGIN_001_OPEN_LOGIN` | `seller` | `login,seller,p0,smoke,navigate` | 打开供应商 seller 登录入口 |
| `SELLER_LOGIN_001` | `SELLER_LOGIN_001_SUBMIT_VALID` | `seller` | `login,seller,p0,smoke,submit` | 使用供应商有效账号提交登录 |
| `SELLER_LOGIN_001` | `SELLER_LOGIN_001_ASSERT_HOME` | `seller` | `login,seller,p0,smoke,assert` | 校验进入供应商 seller 已登录页面 |
| `SELLER_LOGIN_002` | `SELLER_LOGIN_002_LOGIN_FIRST` | `seller_logout` | `login,seller,p0,smoke,prepare` | 先登录进入供应商 seller |
| `SELLER_LOGIN_002` | `SELLER_LOGIN_002_LOGOUT` | `seller_logout` | `login,seller,p0,smoke,logout` | 执行供应商 seller 退出登录 |
| `SELLER_LOGIN_002` | `SELLER_LOGIN_002_ASSERT_LOGOUT` | `seller_logout` | `login,seller,p0,smoke,assert` | 校验供应商 seller 退出后离开已登录状态 |

## 执行方式

在项目根目录执行全部登录用例：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\电商\登录 --browser chromium --headless --output-format json
```

只执行维修厂 mall 登录模块：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\电商\登录 --browser chromium --headless --group mall --output-format json
```

只执行管理中心 admin 登录模块：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\电商\登录 --browser chromium --headless --group admin --output-format json
```

只执行供应商 seller 登录模块：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\电商\登录 --browser chromium --headless --group seller --output-format json
```

只执行维修厂退出链路：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\电商\登录 --browser chromium --headless --group mall_logout --output-format json
```

只执行管理中心退出链路：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\电商\登录 --browser chromium --headless --group admin_logout --output-format json
```

只执行供应商退出链路：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\电商\登录 --browser chromium --headless --group seller_logout --output-format json
```

按标签执行整个登录模块：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\电商\登录 --browser chromium --headless --tag login --output-format json
```

## 当前验证结果

- XML、模型和数据表 dry-run 校验通过，7 个用例均可被 RodSki 加载。
- 全量执行已实测通过：7 个默认用例全部 PASS，覆盖管理中心、维修厂和供应商三端登录/退出链路。
- `--group admin` 已实测通过：管理中心账号 `mandy / Init@1125!@#$` 可登录 admin，且未登录访问认证拦截用例通过。
- `--group admin_logout` 已实测通过：管理中心账号登录后可通过统一退出地址离开已登录状态。
- `--group mall` 已实测通过：维修厂账号 `13119909586 / 123456Aa` 可登录 mall。
- `--group mall_logout` 已实测通过：维修厂账号登录后可通过统一退出地址离开已登录状态。
- `--group seller` 已实测通过：供应商账号 `ksseller1 / Init@1125` 可登录 seller。
- `--group seller_logout` 已实测通过：供应商账号登录后可通过统一退出地址离开已登录状态。

## 维护说明

- 登录页由统一认证链路提供，`PassportLogin` 模型使用多优先级定位器兼容账号登录页签、账号框、密码框、协议勾选和登录按钮。
- `admin`、`mall` 和 `seller` 登录成功断言使用页面 URL、登录控件消失、业务关键词和退出入口综合判断，以降低不同门户首页结构差异带来的误判。
- 如果后续页面加入验证码、短信校验或二次认证，需要在对应登录 scenario 中补充人工暂停步骤或验证码处理步骤。
