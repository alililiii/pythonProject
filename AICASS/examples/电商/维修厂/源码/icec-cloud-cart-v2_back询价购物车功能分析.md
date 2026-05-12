# icec-cloud-cart-v2_back 代码功能分析

> 说明：本文基于 `icec-cloud-cart-v2_back` 工程目录、Maven 模块、启动配置、核心应用服务、接口门面、领域对象、基础设施依赖和数据库脚本整理。该工程体量较大，以下内容侧重于项目定位、功能边界、核心业务链路和维护风险，不是逐类逐方法的完整源码注释。

## 1. 项目定位

`icec-cloud-cart-v2_back` 是电商供应商体系中的新版购物车后端工程。根工程 `pom.xml` 中的描述是 `New Cart Service Project Model`，README 中也明确该工程是“新版购物车工程”。

从代码结构和依赖关系看，它不是一个只做购物车增删改查的轻量服务，而是交易链路中承接“商品/询价/报价进入结算和下单前”的核心中台服务，主要负责：

- 购物车创建、查询、加购、删除、清空和数量修改。
- 按渠道处理购物车明细去重、替换和数量累加规则。
- 维护购物车项选中状态、发票类型、服务门店、促销信息和售后政策。
- 组织结算页初始化、立即购买、优惠计算、运费计算、发票校验和库存校验。
- 连接订单提交服务，把结算结果转换成下单请求。
- 监听订单提交事件，在订单成功后清理对应购物车项。
- 定时清理过期询价购物车数据。

因此，该工程位于商品、报价、询价、促销、优惠券、运费、发票、库存和订单提交之间，是购物车与结算域的业务编排服务。

## 2. 工程结构

根工程是 Maven 多模块项目：

- 根工程：`icec-cloud-cart-v2`
- 服务模块：`icec-cloud-cart-service`
- Web 模块：`icec-cloud-cart-web`

### 2.1 服务模块

核心代码集中在：

`icec-cloud-cart-service/src/main/java/com/casstime/ec/cloud/cart`

主要分层如下：

- `interfaces`：对外接口层，包含 Facade、DTO 转换、校验器和接口入参出参适配。
- `application`：应用服务层，负责购物车、结算、立即购买等业务流程编排。
- `domain`：领域层，包含购物车、购物车项、结算、商品、促销、价格、买家、卖家、门店、发票、售后等领域模型与领域服务接口。
- `infrastructure`：基础设施层，包含 Feign 客户端、MySQL 持久化、Redis 工具、消息事件、XXL Job、外部领域服务实现和通用工具。

这种结构接近 DDD 分层风格：接口层负责协议适配，应用层负责用例编排，领域层表达业务模型和规则，基础设施层承接远程服务、数据库、缓存、消息和任务调度。

### 2.2 Web 模块

`icec-cloud-cart-web` 主要包含 Freemarker 模板和静态资源：

- `src/main/resources/webapp/templates/cart`
- `src/main/resources/webapp/templates/error`
- `src/main/resources/webapp/templates/includes`
- `src/main/resources/webapp/static`

从目录和依赖看，它更像历史购物车页面或页面壳资源模块。当前购物车核心能力仍然集中在 `icec-cloud-cart-service`。

## 3. 启动与配置

服务启动类位于：

`icec-cloud-cart-service/src/main/java/com/casstime/ec/cloud/WebApplication.java`

启动类启用了以下关键能力：

- `@SpringBootApplication`
- `@EnableDiscoveryClient`
- `@EnableFeignClients`
- `@PrepareConfigurations`
- `@EnableAsync`
- `@EnableCaching`
- `@EnabledUniqueId(enableSnowflake = true)`
- `@EnableMessage`

这说明该服务具备：

- Spring Boot 应用启动能力。
- 注册中心服务发现能力。
- Feign 远程服务调用能力。
- 统一配置加载能力。
- 异步处理能力。
- 缓存能力。
- 雪花算法唯一 ID 生成能力。
- 消息收发能力。

`bootstrap.yml` 中的关键配置包括：

- 默认端口：`10031`
- 应用名：`cart-service-v2`
- 配置中心按 `alpha`、`hwbeta`、`prod` 等环境切换。
- `casslog.accessLogEnabled: true`，开启访问日志。
- XXL Job 执行器名称：`cart-job-executor`
- XXL Job 执行器端口：`10025`

从配置看，该服务被设计为注册到微服务体系中运行，依赖配置中心、注册中心、Redis、数据库、消息组件和任务调度平台。

## 4. 核心业务功能

## 4.1 购物车基础能力

购物车主流程由 `CartApplication` 承担，接口层通过 `CartFacade` 暴露能力。

主要功能包括：

- 查询购物车。
- 添加商品到购物车。
- 删除购物车项。
- 按询价单删除购物车项。
- 清空购物车。
- 修改购物车项。
- 修改购物车项数量。
- 修改购物车项选中状态。
- 修改购物车项发票类型。
- 修改服务门店。
- 修改或移除促销信息。
- 查询购物车商品数量。
- 按 ID 批量查询购物车项。
- 查询失效购物车项。
- 计算满减。
- 查询免邮标签。

`CartApplication` 在加购和修改时不仅处理购物车表数据，还会同时处理价格校验、商品推荐价校验、询价商品售后政策、发票类型、服务门店、促销和选中状态等扩展信息。

## 4.2 加购与重复规则

加购逻辑由 `CartApplication` 编排，实际保存由 `AddToCartService` 处理。

关键特点如下：

- 加购时会按买家和操作人身份创建或复用购物车。
- 加购过程使用分布式锁，锁 key 形如 `cart_handler_key_%s`，用于降低并发加购导致重复数据或数量错误的风险。
- 加购前会执行重复数据移除、价格校验、推荐价校验和特殊商品费用处理。
- 购物车项保存时会根据不同渠道采用不同重复判定规则。

不同业务场景的去重规则大致如下：

- 商城购物车：同一 `cartId + channel + productId` 视为同一商品，重复加购时数量累加。
- 定向采购购物车：同一 `cartId + channel + productId` 视为同一商品，重复加购时数量累加。
- 询价购物车：通常按 `cartId + channel + resolveId` 判断重复。
- 轮胎等特殊询价场景：会结合 `userNeedsItemId` 判断具体需求项。
- 询价重复加购时更偏向替换旧项，而不是简单累加数量。

这些规则说明系统需要同时支撑普通商城购买、询价购买、定向采购和特殊品类询价，购物车项不是单纯的 SKU 行，而是带有业务上下文的交易明细。

## 4.3 购物车项状态与扩展信息

购物车项承载的信息较多，除了商品 ID 和数量，还会关联：

- 商品信息。
- 价格信息。
- 促销信息。
- 优惠调整项。
- 发票类型。
- 售后政策。
- 服务门店。
- 询价信息。
- 报价信息。
- 商品属性。
- 卖家和门店信息。
- 是否可见、是否删除、是否过期等状态。

购物车项选中状态通过 `RedisUtilsV2` 保存到 Redis 中，而不是完全依赖数据库字段。这种设计有利于降低高频勾选操作对数据库的写入压力，但也要求结算和查询逻辑正确合并数据库数据与 Redis 状态。

## 4.4 结算能力

结算主流程由 `SettleApplication` 承担，接口层通过 `SettleFacade` 暴露能力。

主要功能包括：

- 从购物车发起结算。
- 立即购买结算。
- 初始化结算页默认数据。
- 计算结算价格。
- 查询平台优惠券。
- 查询店铺优惠券。
- 选择店铺优惠券。
- 修改结算发票类型。
- 校验商品发票库存。
- 查询运费。
- 提交询价校验。
- 提交订单。
- 再次加入购物车。
- 删除定向采购购物车数据。
- 删除结算临时购物车项。
- 检查合同签署状态。
- 发起合同签署。

普通结算流程会先获取购物车和购物车项，校验前端提交的购物车项数量是否与后端一致，再执行结算态、库存、发票库存等校验，最后创建 `Settle` 结算记录。

## 4.5 立即购买

立即购买相关逻辑主要分布在：

- `SettleApplication`
- `ImmediateCheckoutApplication`
- `SettleService`
- 各类 `ImmediateCheckoutServiceI` 扩展实现

立即购买不会依赖用户已有购物车，而是构造临时购物车上下文。代码中使用类似 `BUY_IMMEDIATE_CART_ID` 的虚拟购物车 ID 表达“立即购买”场景。

立即购买流程的重点包括：

- 按场景构造临时购物车项。
- 校验库存和结算状态。
- 保存结算单。
- 保存结算关联的临时购物车项。
- 进入后续价格计算和订单提交流程。

`ImmediateCheckoutApplication` 通过扩展点工厂按场景选择处理器，支持询价报价、商城购买、询价终端门店等不同业务入口。这说明系统已经把立即购买视为多场景扩展点，而不是一个固定流程。

## 4.6 价格、优惠、运费与发票

该工程在结算阶段会聚合多个外部能力：

- 价格计算。
- 平台优惠券。
- 店铺优惠券。
- 店铺促销。
- 满减。
- 金币抵扣。
- 运费计算。
- 免邮标签。
- 预售定金和尾款。
- 发票类型和发票库存。
- 售后政策。

价格计算主要通过 `CalculateDomainService` 及其基础设施实现对接外部计价服务。优惠券相关能力通过 `PlatformCouponService`、`StoreCouponService` 等服务封装。运费和免邮通过物流、地址、门店和免邮标签相关服务组合完成。

发票相关逻辑贯穿购物车和结算两个阶段：

- 加购询价商品时可能根据门店询价分组更新发票类型。
- 修改购物车项或结算项时需要维护发票类型。
- 结算和下单前会校验商品发票库存。
- 下单异常时部分错误码会触发发票类型或促销信息更新。

这说明发票不是后置展示字段，而是会影响结算可用性和下单成功率的核心交易约束。

## 4.7 提交订单

订单提交入口在 `SettleFacade` 中，应用层会先做结算计算和业务校验，再组装订单提交 DTO。

主要流程包括：

- 校验提交订单请求。
- 调用结算计算，刷新价格、优惠、运费等结果。
- 组装 `OrderSubmitDTO` 或立即购买场景的 `SubmitOrderRequestDTO`。
- 调用 `OrderSubmitService` 对接订单提交服务。
- 根据下单返回结果处理异常错误码。
- 必要时更新发票类型或促销信息。

因此，购物车服务在下单前承担了“交易快照整理”的职责，需要把购物车和结算上下文转换成订单系统可识别的提交请求。

## 4.8 事件与定时清理

基础设施层包含订单提交事件处理器：

`OrderSubmittedEventHandler`

该处理器订阅订单提交相关消息，消费者组为 `cart`。订单提交成功后，它会从订单明细的 `objectId` 中提取购物车项 ID，并删除对应购物车项。

定时任务由：

`DeleteCartItemJobHandler`

负责。该任务通过 XXL Job 调度，按配置天数清理过期询价购物车项，底层调用 `CartItemService.deleteExpiredItems(day)`。

这两类机制分别解决：

- 下单成功后的购物车自动清理。
- 询价购物车长期残留数据清理。

## 5. 对外接口能力

## 5.1 CartFacade

`CartFacade` 是购物车相关能力的主要接口门面，包含：

- `getCart`
- `addToCart`
- `modifyCartItem`
- `removeCartItem`
- `removeCartItemByInquiryId`
- `clearCart`
- `modifyCartItemInvoiceType`
- `getCartItemCount`
- `getCartItemAllCount`
- `modifyFacility`
- `modifyPromotion`
- `removePromotion`
- `modifyCartItemQuantity`
- `listCartItemByIds`
- `validItemInvoice`
- `calculateFullOff`
- `findExpiredCartItemIds`
- `findPromotions`
- `findFreePostLabels`
- `changeSelectedState`

该接口体现了购物车服务不是只有基本 CRUD，而是把购物车中的促销、发票、门店、数量、选中状态和结算前校验都统一封装。

## 5.2 SettleFacade

`SettleFacade` 是结算和下单相关能力的主要接口门面，包含：

- `checkout`
- `buyNow`
- `immediateCheckout`
- `getDefaultBySettleId`
- `submitInquiryValid`
- `getLogisticsFee`
- `calculateSettlePrice`
- `submitOrder`
- `submitBuyOrder`
- `listPlatformCoupons`
- `listStoreCoupons`
- `chooseStoreCoupon`
- `modifyInvoiceType`
- `validItemInvoice`
- `listCartItemByIds`
- `getCart`
- `addToCartAgain`
- `deleteDirectionalCartData`
- `deleteSettleCartItems`
- `checkSignContract`
- `signContract`

该接口说明结算层已经覆盖从结算页初始化到订单提交的完整前置链路。

## 6. 领域模型

主要领域对象包括：

- 购物车：`Cart`
- 购物车项：`CartItem`
- 购物车项关联：`CartItemAssoc`
- 结算单：`Settle`
- 调整项：`Adjustment`
- 售后政策：`AftersalePolicy`
- 商品属性：`Attribute`
- 买家：`Buyer`
- 操作人：`Operator`
- 商品：`Product`
- 价格：`Price`
- 促销：`Promotion`
- 卖家：`Seller`
- 门店：`Store`
- 服务门店：`Facility`
- 询价信息：`Inquiry`
- 询价需求：`InquiryNeed`
- 物流费用：`LogisticsFee`
- 免邮/物流相关结果：`WhoLionLogisticsFee`

结算计算相关参数和结果对象包括：

- `CalculateContext`
- `CalculateLogisticsParam`
- `CouponResult`
- `DepositAndRemainder`
- `DiscountAmountResult`
- `FullOffResult`
- `GoldCoinResult`
- `PaymentTypeResult`
- `SaveCartItemParam`
- `StoreAndDeliveryParam`

这些模型说明购物车项本身是交易明细载体，同时聚合了商品、报价、询价、促销、服务、售后和发票等上下文。

## 7. 数据模型与表结构

基础设施层的 MySQL 持久化对象包括：

- `CartDO`
- `CartItemDO`
- `CartItemAttributeDO`
- `CartItemAssocDO`
- `CartItemAdjustmentDO`
- `CartItemPromotionDO`
- `AftersalePolicyDO`
- `SettleDO`
- `SettleCartItemDO`
- `StoreDO`

SQL 脚本 `cart-refactor.sql` 显示该工程经历过购物车重构，主要动作包括：

- 将购物车相关表从 `ec_order` 迁移到 `ec_cart`。
- 新增 `cart_item_adjustment`，用于保存购物车项价格调整、费用、优惠等信息。
- 新增 `cart_item_promotion`，用于保存购物车项促销信息。
- 新增 `settle_cart_item`，用于保存结算关联购物车项。
- 为购物车买家/操作人维度增加唯一索引。
- 将钉盒费、流向调整等历史字段迁移到调整项表。
- 调整 `cart_item.product_id` 字段处理方式。
- 增加 `is_visible`、`delete_at` 等字段，用于可见性和软删除/过期管理。
- 增加询价购物车过期删除配置 `DELETE_OUT_OF_INQUIRY`。

这说明新版本购物车的一个重要目标，是把原本散落在订单域或购物车明细中的扩展数据抽象成更清晰的购物车项、调整项、促销项和结算关联数据。

## 8. 外部服务依赖

该服务通过 Feign 和领域服务封装依赖大量外部系统。常见客户端包括：

- 商品相关：`ProductClient`、`ProductBrandClient`、`ProductBizCatClient`、`ProductInventory` 相关依赖。
- 报价/询价相关：`InquiryClient`、`InquiryTagClient`、`QuotationReadOnlyClient`、`QuotationProductReadOnlyClient`、`QuotationAttributeClient`、`QuotePriceClient`、`DemandReadonlyClient`。
- 促销/优惠相关：`Discount4Client`、`CouponClient`、`MoneyOffRuleClient`、`SupplierPromotionConfigClient`。
- 计价相关：`CalculateClient`。
- 订单相关：`OrderSubmitClient`、`BuySubmitClient`、`BuyContractClient`。
- 门店/服务设施相关：`StoreClient`、`StoreFacilityRelationClient`、`FacilityClient`、`StoreAfterPolicyClient`。
- 发票相关：`InvoiceConfigClient`、`StoreItemInvoiceClient`、`ItemInvoiceInventoryClient`。
- 物流/地址相关：`SettleAvailableLogisticsClient`、`LogisticsHistoryClient`、`PostAddressClient`、`TmsLocationClient`、`PinkageLabelClient`。
- 用户/企业相关：`Userv2Client`、`Companyv2Client`、`CompanyProfileClient`、`CustomerGroupClient`、`VendorClient`。
- 配置和开关相关：`FeatureToggleClient`。

从依赖数量可以看出，购物车和结算服务是一个强编排型服务。它不拥有所有业务数据，但在交易前置阶段会聚合多个系统的数据并做一致性判断。

## 9. 技术架构特点

该工程的主要技术特点包括：

- 基于 Spring Boot `1.4.2.RELEASE` 和 Spring Cloud `Camden.SR3`。
- 使用 Eureka/Feign 进行服务发现和远程调用。
- 使用 Redis 保存部分高频状态，例如购物车项选中状态。
- 使用 MySQL 持久化购物车、购物车项、调整项、促销项、结算项等核心数据。
- 使用 MapStruct 进行对象转换。
- 使用 PageHelper 进行分页支持。
- 使用 HikariCP 作为数据库连接池。
- 使用 XXL Job 执行购物车过期数据清理。
- 使用消息组件消费订单提交事件。
- 使用分布式锁控制购物车并发修改。
- 使用雪花 ID 生成全局唯一业务 ID。
- 使用扩展点工厂支持立即购买等多场景差异化流程。

架构上，它是典型的老 Spring Cloud 微服务项目，业务分层比较明确，但外部依赖较多，服务间协作链路较长。

## 10. 关键业务链路

### 10.1 普通加购链路

1. 接口层接收加购请求。
2. `CartApplication` 获取或创建买家购物车。
3. 按买家/购物车维度加分布式锁。
4. 校验商品、价格、推荐价和特殊费用。
5. 组装购物车项、属性、调整项、促销和售后信息。
6. `AddToCartService` 按渠道规则判断重复项。
7. 保存或更新购物车项。
8. 必要时更新询价商品发票类型和售后政策。

### 10.2 购物车结算链路

1. 前端提交选中的购物车项。
2. `SettleApplication` 查询购物车和购物车项。
3. 校验购物车项数量和状态是否一致。
4. 校验商品结算态、库存和发票库存。
5. 创建 `Settle` 结算单。
6. 初始化结算页数据。
7. 计算价格、优惠、运费、满减、金币和预售金额。
8. 返回结算页展示所需的数据。

### 10.3 立即购买链路

1. 接口层接收立即购买请求。
2. `ImmediateCheckoutApplication` 根据场景选择扩展处理器。
3. 构造临时购物车项和虚拟购物车上下文。
4. 校验库存、结算态和发票约束。
5. 保存结算单和临时结算购物车项。
6. 进入结算计算或下单流程。

### 10.4 提交订单链路

1. 接口层接收提交订单请求。
2. 执行提交前校验。
3. 调用结算计算刷新交易金额。
4. 组装订单提交请求。
5. 调用订单提交服务。
6. 根据订单服务返回结果处理异常。
7. 订单成功后通过事件机制清理购物车项。

## 11. 维护风险与关注点

### 11.1 外部依赖较多

该服务依赖商品、询价、报价、促销、优惠券、物流、地址、发票、库存、订单、用户、企业、门店等多个系统。任何一个依赖接口变更、超时或返回数据不一致，都可能影响购物车结算和下单。

维护时应重点关注 Feign 客户端 DTO 兼容性、错误码处理、超时策略、降级策略和接口幂等性。

### 11.2 购物车项语义复杂

购物车项不只是商品数量行，还可能包含询价、报价、促销、售后、发票、门店和费用调整信息。新增业务字段时需要判断它应该放在：

- 购物车主表。
- 购物车项表。
- 属性表。
- 调整项表。
- 促销表。
- 结算关联表。
- Redis 状态。

否则容易继续扩大 `CartItem` 的复杂度。

### 11.3 渠道差异要谨慎处理

商城、询价、定向采购、预售和终端门店等场景在加购、去重、价格、库存、发票和结算上都有差异。修改通用逻辑时，需要确认不会破坏特殊渠道规则。

尤其要注意：

- 询价重复加购的替换规则。
- 商城和定向采购的数量累加规则。
- 特殊品类按需求项判断重复的规则。
- 立即购买虚拟购物车 ID 的处理。

### 11.4 数据一致性依赖多种机制

系统同时使用数据库、Redis、消息和定时任务维护状态：

- 数据库保存购物车和结算主数据。
- Redis 保存购物车项选中状态。
- 消息用于订单成功后清理购物车。
- XXL Job 用于清理过期询价购物车项。

因此需要关注消息消费失败、Redis 状态丢失、定时任务未执行、重复消费和数据库事务边界等问题。

### 11.5 技术栈版本较老

服务基于 Spring Boot `1.4.2.RELEASE` 和 Spring Cloud `Camden.SR3`，属于较老版本体系。升级或引入新组件时，需要重点评估：

- Spring Cloud 兼容性。
- Feign 行为差异。
- 配置中心和注册中心兼容性。
- 老版本依赖中的安全漏洞。
- Java 版本约束。

## 12. 总结

`icec-cloud-cart-v2_back` 是电商交易链路中的新版购物车与结算前置服务。它的核心价值不只是保存购物车商品，而是把商品、报价、询价、促销、优惠券、运费、发票、库存、售后、合同和订单提交等能力串联起来，为用户从“选择商品”到“提交订单”之间的复杂交易流程提供统一编排。

从代码形态看，工程采用接口层、应用层、领域层、基础设施层的分层方式，业务职责清晰，但外部依赖和场景分支较多。后续维护时，应优先保护加购去重规则、结算计算链路、发票/库存校验、订单提交转换和订单成功清理这几条关键路径。

整体判断：该工程是供应商电商体系中的核心交易前置服务，适合按“购物车域 + 结算域 + 外部服务编排”的角度理解和维护。
