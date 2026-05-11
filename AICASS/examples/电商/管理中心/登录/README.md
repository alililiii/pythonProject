# 管理中心登录模块 RodSki 自动化用例

## 生成依据

- `src/main/resources/bootstrap.yml`
  - `server.port: 9805`
  - `server.contextPath: /systemMgr`
- `src/main/java/com/casstime/ec/cloud/web/sysmgr/index/IndexController.java`
  - 登录后首页入口：`GET /admin`
  - 首页模板：`templates/index/index.ftl`
  - 当前登录账号模型字段：`userId`
- `src/main/resources/webapp/templates/index/index.ftl`
  - 管理中心首页标题和 Logo
  - 当前用户隐藏字段：`#userLogin`
  - 退出入口：`/logout`
- `src/main/java/com/casstime/ec/cloud/web/handler/AuthInterceptor.java`
  - `/systemMgr` 下请求读取当前用户
  - 未登录不放行
  - 无权限跳转 `/error/403`

## 目录结构

```text
AICASS/examples/电商/管理中心/登录/
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
| `LOGIN_001` | P0 | 是 | 未登录访问 `/systemMgr/admin` 应被认证拦截 |
| `LOGIN_002` | P0 | 是 | 有效账号登录后进入管理中心首页 |
| `LOGIN_003` | P0 | 是 | 登录后点击 `/logout` 应退出登录态 |
| `LOGIN_004` | P1 | 否 | 错误密码登录失败提示，默认关闭以避免账号锁定 |

## Scenario 拆分

RodSki v6.3+ 支持在同一个 `<case>` 的 `<test_case>` 内使用 `<scenario>` 组织主链路步骤。登录模块已按“进入入口 / 提交动作 / 结果断言”的方式拆分 scenario，并通过 `depends` 表达链路依赖。

| 用例ID | Scenario ID | 分组 | 标签 | 场景说明 |
| --- | --- | --- | --- | --- |
| `LOGIN_001` | `LOGIN_001_ACCESS_ADMIN` | `auth` | `login,p0,smoke,unauthenticated` | 未登录访问管理中心首页 |
| `LOGIN_001` | `LOGIN_001_ASSERT_BLOCKED` | `auth` | `login,p0,smoke,assert` | 校验未登录访问被认证拦截 |
| `LOGIN_002` | `LOGIN_002_OPEN_LOGIN` | `positive` | `login,p0,smoke,navigate` | 打开管理中心登录入口 |
| `LOGIN_002` | `LOGIN_002_SUBMIT_VALID` | `positive` | `login,p0,smoke,submit` | 使用有效账号提交登录 |
| `LOGIN_002` | `LOGIN_002_ASSERT_HOME` | `positive` | `login,p0,smoke,assert` | 校验进入管理中心首页 |
| `LOGIN_003` | `LOGIN_003_LOGIN_FIRST` | `logout` | `login,p0,smoke,prepare` | 先登录进入管理中心首页 |
| `LOGIN_003` | `LOGIN_003_CLICK_LOGOUT` | `logout` | `login,p0,smoke,logout` | 点击管理中心退出入口 |
| `LOGIN_003` | `LOGIN_003_ASSERT_LOGOUT` | `logout` | `login,p0,smoke,assert` | 校验退出后离开已登录状态 |
| `LOGIN_004` | `LOGIN_004_OPEN_LOGIN` | `negative` | `login,p1,negative,navigate` | 打开管理中心登录入口 |
| `LOGIN_004` | `LOGIN_004_SUBMIT_INVALID` | `negative` | `login,p1,negative,submit` | 使用错误密码提交登录 |
| `LOGIN_004` | `LOGIN_004_ASSERT_REJECTED` | `negative` | `login,p1,negative,assert` | 校验错误密码被拒绝 |

## 执行方式

在项目根目录或任意目录执行：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\电商\管理中心\登录 --browser chromium
```

无头执行：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\电商\管理中心\登录 --browser chromium --headless
```

只执行 P0：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\电商\管理中心\登录 --priority P0
```

按 scenario 标签临时筛选，例如执行冒烟场景：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\电商\管理中心\登录 --tag smoke
```

按 scenario 分组临时筛选，例如只执行退出链路：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\电商\管理中心\登录 --group logout
```

生成 HTML 报告：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\电商\管理中心\登录 --report html --output D:\Documents\pythonProject\AICASS\examples\电商\管理中心\登录\result
```

## 环境说明

- 默认访问地址写在 `data/globalvalue.xml` 的 `Env.admin_url` 中：`https://ec-hwbeta.casstime.com/admin#`。
- 如果应用部署在测试环境，请修改 `Env.base_url` 和 `Env.admin_url`。
- 登录页由统一认证或 Spring Security 链路提供，当前工程内没有独立登录页模板。因此 `PassportLogin` 模型使用常见账号、密码、提交按钮定位器，并配置了多个优先级定位。
- 如果登录页包含验证码、短信校验或二次认证，需要在 `case/login_cases.xml` 中补充人工暂停步骤或对应验证码处理步骤。
