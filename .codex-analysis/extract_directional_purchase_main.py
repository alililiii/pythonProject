import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError


URL = "https://ec-hwbeta.casstime.com/seller#/order/directional-purchase"
USERNAME = "ksseller1"
PASSWORD = "Init@1125"
OUT = Path(".codex-analysis/directional_purchase_main_elements.json")
SHOT = Path(".codex-analysis/directional_purchase_main_after_clicks.png")


async def login(page):
    await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
    await page.wait_for_timeout(2000)
    if "passport/login" not in page.url:
        return
    try:
        await page.get_by_text("账号登录", exact=True).click(timeout=3000)
    except Exception:
        pass
    await page.locator("input[name='username']").fill(USERNAME)
    await page.locator("#password").fill(PASSWORD)
    await page.locator("input.btn-submit").click()
    await page.wait_for_timeout(1000)
    try:
        agree = page.get_by_text("同意", exact=True)
        if await agree.count() and await agree.first.is_visible(timeout=2000):
            await agree.first.click()
            await page.wait_for_timeout(500)
            await page.locator("input.btn-submit").click()
    except Exception:
        pass
    try:
        await page.wait_for_load_state("networkidle", timeout=20000)
    except PlaywrightTimeoutError:
        pass
    await page.wait_for_timeout(8000)
    if "directional-purchase" not in page.url:
        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(5000)


async def main():
    requests = []
    responses = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1440, "height": 1100},
            ignore_https_errors=True,
            locale="zh-CN",
        )
        page = await context.new_page()
        page.on("request", lambda req: requests.append({"method": req.method, "url": req.url, "resourceType": req.resource_type}))
        page.on("response", lambda resp: responses.append({"status": resp.status, "url": resp.url}))

        await login(page)

        main = await page.evaluate(
            """
            () => {
              const norm = s => (s || '').replace(/\\s+/g, ' ').trim();
              const visible = (el) => {
                const style = getComputedStyle(el);
                const rect = el.getBoundingClientRect();
                return style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0 && rect.height > 0;
              };
              const root = document.querySelector('.seller-main, main, #root') || document.body;
              const bodyText = norm(root.innerText || root.textContent || '');
              const inputs = Array.from(root.querySelectorAll('input, textarea, select, [role=combobox], .ant-select, .el-select'))
                .filter(visible)
                .map(el => ({
                  tag: el.tagName.toLowerCase(),
                  type: el.getAttribute('type') || '',
                  value: el.value || '',
                  placeholder: el.getAttribute('placeholder') || '',
                  text: norm(el.innerText || el.textContent || ''),
                  className: typeof el.className === 'string' ? el.className : '',
                  disabled: !!el.disabled || el.getAttribute('aria-disabled') === 'true'
                }));
              const buttons = Array.from(root.querySelectorAll('button, [role=button], a, .ant-btn, .el-button'))
                .filter(visible)
                .map(el => ({
                  tag: el.tagName.toLowerCase(),
                  text: norm(el.innerText || el.textContent || el.getAttribute('title') || el.getAttribute('aria-label') || ''),
                  className: typeof el.className === 'string' ? el.className : '',
                  disabled: !!el.disabled || el.getAttribute('aria-disabled') === 'true'
                }))
                .filter(x => x.text);
              const labels = Array.from(root.querySelectorAll('label, .ant-form-item-label, .el-form-item__label, td, th, .label'))
                .filter(visible)
                .map(el => norm(el.innerText || el.textContent || ''))
                .filter(Boolean);
              const tableHeaders = Array.from(root.querySelectorAll('th'))
                .filter(visible)
                .map(el => norm(el.innerText || el.textContent || ''))
                .filter(Boolean);
              const requiredTexts = Array.from(root.querySelectorAll('*'))
                .filter(visible)
                .map(el => norm(el.innerText || el.textContent || ''))
                .filter(t => t.includes('*') && t.length <= 30);
              const warnings = Array.from(root.querySelectorAll('*'))
                .filter(visible)
                .map(el => norm(el.innerText || el.textContent || ''))
                .filter(t => /请选择|请输入|不能为空|最多|提示|警告|失败|成功|总价|商品/.test(t))
                .filter((v, i, a) => v && a.indexOf(v) === i)
                .slice(0, 120);
              return {url: location.href, title: document.title, bodyText, inputs, buttons, labels, tableHeaders, requiredTexts, warnings};
            }
            """
        )

        interactions = []
        for trigger_text in ["查看批量操作指南", "新增商品", "清空全部商品", "下一步"]:
            try:
                locator = page.get_by_text(trigger_text, exact=False).last
                if await locator.count() and await locator.is_visible(timeout=1500):
                    await locator.click(timeout=3000)
                    await page.wait_for_timeout(1200)
                    snapshot = await page.evaluate(
                        """
                        () => {
                          const norm = s => (s || '').replace(/\\s+/g, ' ').trim();
                          const visible = (el) => {
                            const style = getComputedStyle(el);
                            const rect = el.getBoundingClientRect();
                            return style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0 && rect.height > 0;
                          };
                          return {
                            text: norm(document.body.innerText || document.body.textContent || '').slice(0, 4000),
                            dialogs: Array.from(document.querySelectorAll('[role=dialog], .ant-modal, .el-dialog, .modal, .ant-message, .el-message'))
                              .filter(visible).map(el => norm(el.innerText || el.textContent || '')),
                            inputs: Array.from(document.querySelectorAll('input, textarea')).filter(visible).map(el => ({placeholder: el.getAttribute('placeholder') || '', value: el.value || '', disabled: !!el.disabled})),
                            buttons: Array.from(document.querySelectorAll('button, [role=button], a')).filter(visible).map(el => norm(el.innerText || el.textContent || '')).filter(Boolean).slice(-50)
                          };
                        }
                        """
                    )
                    interactions.append({"trigger": trigger_text, "snapshot": snapshot})
                    close = page.locator(".ant-modal-close, .el-dialog__headerbtn, button:has-text('取消'), button:has-text('关闭'), button:has-text('知道了')").first
                    try:
                        if await close.count() and await close.is_visible(timeout=1000):
                            await close.click()
                            await page.wait_for_timeout(600)
                    except Exception:
                        pass
            except Exception as exc:
                interactions.append({"trigger": trigger_text, "error": repr(exc)})

        try:
            await page.screenshot(path=str(SHOT), full_page=True)
        except Exception:
            pass

        result = {
            "main": main,
            "interactions": interactions,
            "requests": [r for r in requests if any(k in r["url"].lower() for k in ["directional", "order", "address", "product", "brand", "company", "store", "customer", "cart", "settle", "invoice"])][-300:],
            "responses": [r for r in responses if any(k in r["url"].lower() for k in ["directional", "order", "address", "product", "brand", "company", "store", "customer", "cart", "settle", "invoice"])][-300:],
        }
        OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
