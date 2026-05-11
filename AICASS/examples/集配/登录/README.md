# 集配三端登录模块 RodSki 自动化用例

## 覆盖范围

本模块整合集配平台三端登录自动化，覆盖买家工作台、卖家工作台和管理中心：

- 买家工作台 buyer：`https://f2b-beta.casstime.com/buyer#/`
- 卖家工作台 seller：`https://f2b-beta.casstime.com/seller#/`
- 管理中心 admin：`https://f2b-beta.casstime.com/admin#`

地址和账号来源：`AICASS/data/平台账户汇总.xlsx`。

## 目录结构

```text
AICASS/examples/集配/登录/
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
| `BUYER_LOGIN_001` | P0 | 是 | 买家工作台账号登录 buyer 后进入买家工作台 |
| `BUYER_LOGIN_002` | P0 | 是 | 买家工作台账号登录 buyer 后退出登录 |
| `SELLER_LOGIN_001` | P0 | 是 | 卖家工作台账号登录 seller 后进入卖家工作台 |
| `SELLER_LOGIN_002` | P0 | 是 | 卖家工作台账号登录 seller 后退出登录 |
| `ADMIN_LOGIN_001` | P0 | 是 | 管理中心未登录访问 admin 应被认证拦截 |
| `ADMIN_LOGIN_002` | P0 | 是 | 管理中心账号登录 admin 后进入管理中心首页 |
| `ADMIN_LOGIN_003` | P0 | 是 | 管理中心账号登录 admin 后退出登录 |

## 测试账号

| 端 | 账号 | 密码 |
| --- | --- | --- |
| 买家工作台 | `17621866086` | `A.123456` |
| 卖家工作台 | `15152005981` | `Cass1713` |
| 管理中心 | `18819450973` | `Cass1713` |

账号数据同时保存在 `data/globalvalue.xml` 和 `data/data.sqlite` 中，RodSki 执行时以 `data.sqlite` 的 `PassportLogin` 数据表为准。

## Scenario 拆分

用例主体使用 RodSki v6.3+ 的 `<scenario>` 结构，按“打开入口 / 提交登录 / 结果断言 / 退出断言”拆分，并通过 `depends` 表达主链路依赖。

| 用例ID | Scenario ID | 分组 | 标签 | 场景说明 |
| --- | --- | --- | --- | --- |
| `BUYER_LOGIN_001` | `BUYER_LOGIN_001_OPEN_LOGIN` | `buyer` | `login,buyer,p0,smoke,navigate` | 打开买家工作台 buyer 登录入口 |
| `BUYER_LOGIN_001` | `BUYER_LOGIN_001_SUBMIT_VALID` | `buyer` | `login,buyer,p0,smoke,submit` | 使用买家工作台有效账号提交登录 |
| `BUYER_LOGIN_001` | `BUYER_LOGIN_001_ASSERT_HOME` | `buyer` | `login,buyer,p0,smoke,assert` | 校验进入买家工作台已登录页面 |
| `BUYER_LOGIN_002` | `BUYER_LOGIN_002_LOGIN_FIRST` | `buyer_logout` | `login,buyer,p0,smoke,prepare` | 先登录进入买家工作台 buyer |
| `BUYER_LOGIN_002` | `BUYER_LOGIN_002_LOGOUT` | `buyer_logout` | `login,buyer,p0,smoke,logout` | 执行买家工作台 buyer 退出登录 |
| `BUYER_LOGIN_002` | `BUYER_LOGIN_002_ASSERT_LOGOUT` | `buyer_logout` | `login,buyer,p0,smoke,assert` | 校验买家工作台 buyer 退出后离开已登录状态 |
| `SELLER_LOGIN_001` | `SELLER_LOGIN_001_OPEN_LOGIN` | `seller` | `login,seller,p0,smoke,navigate` | 打开卖家工作台 seller 登录入口 |
| `SELLER_LOGIN_001` | `SELLER_LOGIN_001_SUBMIT_VALID` | `seller` | `login,seller,p0,smoke,submit` | 使用卖家工作台有效账号提交登录 |
| `SELLER_LOGIN_001` | `SELLER_LOGIN_001_ASSERT_HOME` | `seller` | `login,seller,p0,smoke,assert` | 校验进入卖家工作台已登录页面 |
| `SELLER_LOGIN_002` | `SELLER_LOGIN_002_LOGIN_FIRST` | `seller_logout` | `login,seller,p0,smoke,prepare` | 先登录进入卖家工作台 seller |
| `SELLER_LOGIN_002` | `SELLER_LOGIN_002_LOGOUT` | `seller_logout` | `login,seller,p0,smoke,logout` | 执行卖家工作台 seller 退出登录 |
| `SELLER_LOGIN_002` | `SELLER_LOGIN_002_ASSERT_LOGOUT` | `seller_logout` | `login,seller,p0,smoke,assert` | 校验卖家工作台 seller 退出后离开已登录状态 |
| `ADMIN_LOGIN_001` | `ADMIN_LOGIN_001_ACCESS_ADMIN` | `admin` | `login,admin,p0,smoke,unauthenticated` | 未登录访问管理中心 admin 首页 |
| `ADMIN_LOGIN_001` | `ADMIN_LOGIN_001_ASSERT_BLOCKED` | `admin` | `login,admin,p0,smoke,assert` | 校验管理中心未登录访问被认证拦截 |
| `ADMIN_LOGIN_002` | `ADMIN_LOGIN_002_OPEN_LOGIN` | `admin` | `login,admin,p0,smoke,navigate` | 打开管理中心 admin 登录入口 |
| `ADMIN_LOGIN_002` | `ADMIN_LOGIN_002_SUBMIT_VALID` | `admin` | `login,admin,p0,smoke,submit` | 使用管理中心有效账号提交登录 |
| `ADMIN_LOGIN_002` | `ADMIN_LOGIN_002_ASSERT_HOME` | `admin` | `login,admin,p0,smoke,assert` | 校验进入管理中心 admin 首页 |
| `ADMIN_LOGIN_003` | `ADMIN_LOGIN_003_LOGIN_FIRST` | `admin_logout` | `login,admin,p0,smoke,prepare` | 先登录进入管理中心 admin 首页 |
| `ADMIN_LOGIN_003` | `ADMIN_LOGIN_003_LOGOUT` | `admin_logout` | `login,admin,p0,smoke,logout` | 执行管理中心 admin 退出登录 |
| `ADMIN_LOGIN_003` | `ADMIN_LOGIN_003_ASSERT_LOGOUT` | `admin_logout` | `login,admin,p0,smoke,assert` | 校验管理中心 admin 退出后离开已登录状态 |

## 执行方式

在项目根目录执行全部登录用例：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\集配\登录 --browser chromium --headless --output-format json
```

只执行买家工作台登录模块：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\集配\登录 --browser chromium --headless --group buyer --output-format json
```

只执行卖家工作台登录模块：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\集配\登录 --browser chromium --headless --group seller --output-format json
```

只执行管理中心登录模块：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\集配\登录 --browser chromium --headless --group admin --output-format json
```

只执行买家工作台退出链路：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\集配\登录 --browser chromium --headless --group buyer_logout --output-format json
```

只执行卖家工作台退出链路：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\集配\登录 --browser chromium --headless --group seller_logout --output-format json
```

只执行管理中心退出链路：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\集配\登录 --browser chromium --headless --group admin_logout --output-format json
```

按标签执行整个登录模块：

```powershell
venv\Scripts\rodski.exe run AICASS\examples\集配\登录 --browser chromium --headless --tag login --output-format json
```

## 维护说明

- 当前已完成 RodSki dry-run 校验：7 个用例均可加载。
- 当前已完成全量实跑校验：`venv\Scripts\rodski.exe run AICASS\examples\集配\登录 --browser chromium --headless --output-format json`，7 个用例全部 PASS。
- 登录页由统一认证链路提供，`PassportLogin` 模型使用多优先级定位器兼容账号登录页签、账号框、密码框、协议勾选和登录按钮。
- `buyer`、`seller` 和 `admin` 登录成功断言使用页面 URL、登录控件消失、业务关键词和退出入口综合判断，以降低不同门户首页结构差异带来的误判。
- 如果后续页面加入验证码、短信校验或二次认证，需要在对应登录 scenario 中补充人工暂停步骤或验证码处理步骤。
