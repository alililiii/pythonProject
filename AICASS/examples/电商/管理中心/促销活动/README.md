# 平台促销活动新增/编辑页 RodSki 自动化用例

## 目录

```text
AICASS/examples/管理中心/促销活动/
  case/platform_promotions_add_edit_cases.xml
  model/model.xml
  data/globalvalue.xml
  data/data.sqlite
  fun/
  result/
```

## 覆盖范围

该用例集基于 `平台促销活动新增编辑页场景测试用例.md` 生成，默认执行非破坏性场景：

- 登录后访问平台促销活动新增/编辑页。
- 校验 merchant React 子应用 iframe 加载。
- 校验页面核心分区、字段、默认单选项和促销条件表格。
- 点击空表单保存，验证必填校验。
- 切换促销类型、营销费用、促销叠加规则。
- 新增一项促销条件配置。
- 切换活动对象、活动店铺、活动商品范围。

真实保存活动的用例默认关闭，避免在测试环境创建脏数据。

当前默认可执行用例位于：

```text
case/platform_promotions_add_edit_cases.xml
```

默认执行 7 条 P0/P1 页面加载、认证拦截、静态元素、默认态、必填校验和动态联动用例；取消返回用例默认关闭。

## 组合新增用例

基于补充的排列组合场景，已新增：

```text
case/platform_promotions_combo_cases.xml
```

该文件包含 `PROMO_COMBO_AUTO_001` 到 `PROMO_COMBO_AUTO_020` 共 20 条组合用例，覆盖：

- 商城业务/询价业务。
- 北京市/不限区域。
- 全部客户、指定参与客户、指定不参与客户。
- 满立折、满立减。
- 不设上限、营销费用上限。
- 不叠加、叠加。
- 不限店铺、指定可参与店铺、指定不可参与店铺。
- 指定品质原厂件、指定品牌、指定品类。
- 区域/客户/店铺/品质为空、折扣非法、满减非法、费用上限非法等失败校验组合。

这些组合用例当前均为 `execute="否"`。原因是成功组合会真实创建平台促销活动，失败组合也需要先补齐业务线、区域、客户、店铺、品质等控件的实际可选项和数据清理策略。确认测试环境允许造数并补充保存后查询/清理步骤后，再打开对应用例执行。

组合脚本数据位于 `data/data.sqlite` 的 `PromoCombo` 逻辑表，Case 通过 `PromoCombo.COMBO_001.script` 等数据引用调用，避免在 Case 中硬编码大段表单配置逻辑。

## 执行方式

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\管理中心\促销活动 --browser chromium
```

仅做语法和用例结构校验：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe run D:\Documents\pythonProject\AICASS\examples\管理中心\促销活动 --browser chromium --dry-run
```

数据层校验：

```powershell
D:\Documents\pythonProject\venv\Scripts\rodski.exe data validate D:\Documents\pythonProject\AICASS\examples\管理中心\促销活动
```

当前已验证：

```text
data validate: 3 张逻辑表校验通过
dry-run: 默认 7 条可执行用例验证通过
static references: 28 条 case、3 个 model、31 行数据引用完整
```

## 注意事项

- 页面在管理中心主框架内通过 `iframeCon` 加载 `/admin/merchant#/platform-promotions/add-edit`，断言脚本会进入 iframe 的 `contentDocument`。
- 登录数据保存在 `data/globalvalue.xml` 和 `data/data.sqlite`，当前账号为 `mandy`。
- 如果统一登录页、隐私协议勾选框或促销页组件类名调整，需要同步更新 `model/model.xml` 或 `data/data.sqlite` 中的 `PromoScript` / `PromoCombo` 脚本数据。
