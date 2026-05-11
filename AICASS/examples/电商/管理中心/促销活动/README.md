# 平台促销活动新增/编辑页 RodSki 自动化用例

## 目录

```text
AICASS/examples/电商/管理中心/促销活动/
  case/platform_promotions_add_edit_cases.xml
  case/platform_promotions_combo_cases.xml
  model/model.xml
  data/globalvalue.xml
  data/data.sqlite
  plan/
  result/
```

## 重构依据

本模块按以下材料重构：

- `平台促销活动新增编辑页场景测试用例.md`
- `AICASS/data/02 平台促销活动场景数据.xlsx` 的 `修正场景数据`
- `AICASS/docs/TEST_CASE_WRITING_GUIDE.md` 中 `scenario` 容器与 plan 规则

RodSki 版本为 `6.3.9`，已支持在同一个 `<test_case>` 内用 `<scenario>` 分组步骤。

## 用例结构

### 页面冒烟用例

```text
case/platform_promotions_add_edit_cases.xml
```

默认执行 6 条非破坏性页面用例：

- `PROMO_ADD_001` 登录后直接访问新增页。
- `PROMO_ADD_002` 未登录访问新增页应被认证拦截。
- `PROMO_ADD_004` 页面静态元素完整性。
- `PROMO_ADD_005` 空表单保存必填校验。
- `PROMO_ADD_006` 促销玩法动态联动校验。
- `PROMO_ADD_007` 范围类单选项切换联动校验。

`PROMO_ADD_093` 取消返回用例默认关闭。

### Excel 场景用例

```text
case/platform_promotions_combo_cases.xml
```

该文件已从旧组合矩阵重构为 Excel 对齐的 32 条场景：

- `PC-001` 到 `PC-012`：成功保存场景。
- `PC-N01` 到 `PC-N20`：负向校验场景。

这些场景全部为 `execute="否"`。成功场景会真实创建平台促销活动，负向场景也会触发表单保存校验；执行前需要确认测试环境允许造数，并准备查询、停用或清理策略。

每条 Excel 场景按 `scenario` 拆分：

- `S001`：加载公共场景引擎并确认页面就绪。
- `S002`：填充 Excel 场景数据。
- `S003`：断言保存成功或校验失败。
- `S004`：截图留存。

## 数据与脚本

`data/data.sqlite` 保持 RodSki 的逻辑表结构：

- `PassportLogin`：登录数据。
- `PromoScript`：公共页面断言、公共场景引擎和保存断言。
- `PromoCombo`：32 条 Excel 场景配置脚本。

重构后 `PromoCombo` 不再保存大段重复 UI 操作脚本，而是每行只传入当前场景的 JSON 配置，由 `PromoScript.ScenarioEngine.script` 统一执行 iframe 定位、表单填写、规则表格填充和范围配置。

`data/globalvalue.xml` 中的 `PromoData` 已替换为当前场景使用的数据：

- 客户：`C0437311 小泽维修厂(试点)`、`C0385195 小泽维修厂(非试点)`。
- 客户分组：`PRMANSTO`、`SYSTOMAN`、`OTHERPP`。
- 店铺：`4400056296`、`4400051923`、`4400050889`、`4400055631`。
- 店铺分组：`GRPS01` 到 `GRPS04`。
- 车辆品牌、品质、配件品牌、品类、商品 SKU 与 Excel 修正数据一致。

## 测试计划

```text
plan/promo_add_001_only.xml
plan/promo_smoke.xml
plan/promo_excel_scenarios.xml
```

`promo_smoke.xml` 仅覆盖默认非破坏性页面冒烟用例。`promo_excel_scenarios.xml` 收录 32 条 Excel 场景，但 case 和 scenario 均默认关闭。

## 校验命令

数据层校验：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe data validate D:\Documents\pythonProject\AICASS\examples\电商\管理中心\促销活动
```

dry-run 结构校验：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\电商\管理中心\促销活动 --browser chromium --dry-run --output-format json
```

执行默认冒烟用例：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\电商\管理中心\促销活动 --browser chromium
```

## 注意事项

- 页面通过管理中心 `#iframeCon` 加载 `/admin/merchant#/platform-promotions/add-edit`，所有页面断言和表单填写都需要进入 iframe。
- Excel 修正数据中，满立减的平台分摊是金额，满立折的平台分摊是比例；自动化脚本按该规则原样填充。
- `PC-*` 成功场景默认关闭，避免产生平台促销活动脏数据。
- 如统一登录、隐私协议弹窗、促销页控件文案或弹窗结构变化，需要同步调整 `data.sqlite` 中 `PromoScript.ScenarioEngine.script`。
