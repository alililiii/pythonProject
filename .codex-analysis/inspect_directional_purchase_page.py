import asyncio
import json
import re
from pathlib import Path

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError


URL = "https://ec-hwbeta.casstime.com/seller#/order/directional-purchase"
USERNAME = "ksseller1"
PASSWORD = "Init@1125"
OUT = Path(".codex-analysis/directional_purchase_page_elements.json")
SHOT = Path(".codex-analysis/directional_purchase_page.png")


async def fill_first(page, selectors, value):
    for selector in selectors:
        locator = page.locator(selector)
        try:
            if await locator.count():
                first = locator.first
                if await first.is_visible(timeout=1500):
                    await first.fill(value)
                    return selector
        except Exception:
            continue
    return None


async def click_first(page, selectors):
    for selector in selectors:
        locator = page.locator(selector)
        try:
            if await locator.count():
                first = locator.first
                if await first.is_visible(timeout=1500):
                    await first.click()
                    return selector
        except Exception:
            continue
    return None


async def collect_elements(page):
    return await page.evaluate(
        """
        () => {
          const visible = (el) => {
            const style = getComputedStyle(el);
            const rect = el.getBoundingClientRect();
            return style && style.visibility !== 'hidden' && style.display !== 'none' && rect.width > 0 && rect.height > 0;
          };
          const textOf = (el) => (el.innerText || el.textContent || el.getAttribute('aria-label') || el.getAttribute('title') || '').replace(/\\s+/g, ' ').trim();
          const attrs = (el) => ({
            tag: el.tagName.toLowerCase(),
            text: textOf(el),
            id: el.id || '',
            name: el.getAttribute('name') || '',
            type: el.getAttribute('type') || '',
            placeholder: el.getAttribute('placeholder') || '',
            title: el.getAttribute('title') || '',
            ariaLabel: el.getAttribute('aria-label') || '',
            role: el.getAttribute('role') || '',
            className: typeof el.className === 'string' ? el.className : '',
            disabled: !!el.disabled || el.getAttribute('aria-disabled') === 'true'
          });

          const buttons = Array.from(document.querySelectorAll('button, [role=button], a, .ant-btn, .el-button'))
            .filter(visible).map(attrs);
          const inputs = Array.from(document.querySelectorAll('input, textarea, select, .ant-select, .el-select, [contenteditable=true]'))
            .filter(visible).map(attrs);
          const tableHeaders = Array.from(document.querySelectorAll('th, .ant-table-thead .ant-table-cell, .el-table__header th, .vxe-header--column'))
            .filter(visible).map(textOf).filter(Boolean);
          const labels = Array.from(document.querySelectorAll('label, .ant-form-item-label, .el-form-item__label, .form-label'))
            .filter(visible).map(textOf).filter(Boolean);
          const tabs = Array.from(document.querySelectorAll('[role=tab], .ant-tabs-tab, .el-tabs__item'))
            .filter(visible).map(attrs);
          const dialogs = Array.from(document.querySelectorAll('[role=dialog], .ant-modal, .el-dialog, .modal'))
            .filter(visible).map(attrs);
          const menuItems = Array.from(document.querySelectorAll('.ant-menu-item, .el-menu-item, [role=menuitem]'))
            .filter(visible).map(attrs);
          const pageText = textOf(document.body).slice(0, 8000);
          return {
            title: document.title,
            url: location.href,
            buttons,
            inputs,
            tableHeaders,
            labels,
            tabs,
            dialogs,
            menuItems,
            pageText
          };
        }
        """
    )


async def main():
    requests = []
    responses = []
    console = []

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
        page.on("console", lambda msg: console.append({"type": msg.type, "text": msg.text[:500]}))

        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(2500)

        login_before = await collect_elements(page)
        try:
            account_tab = page.get_by_text("账号登录", exact=True)
            if await account_tab.count() and await account_tab.first.is_visible(timeout=1500):
                await account_tab.first.click()
                await page.wait_for_timeout(800)
        except Exception:
            pass
        username_selector = await fill_first(
            page,
            [
                "#userLoginName",
                "#username",
                "#loginName",
                "input[name='username']",
                "input[name='userName']",
                "input[name='loginName']",
                "input[name='account']",
                "input[placeholder*='账号']",
                "input[placeholder*='登录名']",
                "input[placeholder*='账号']",
                "input[placeholder*='用户名']",
                "input[placeholder*='手机']",
                "input[type='text']",
            ],
            USERNAME,
        )
        password_selector = await fill_first(
            page,
            [
                "#password",
                "input[name='password']",
                "input[placeholder*='密码']",
                "input[type='password']",
            ],
            PASSWORD,
        )
        clicked_selector = None
        if username_selector and password_selector:
            clicked_selector = await click_first(
                page,
                [
                    "input.btn-submit",
                    "button:has-text('登录')",
                    "button:has-text('登 录')",
                    "button[type='submit']",
                    ".login button",
                    ".ant-btn-primary",
                    ".el-button--primary",
                ],
            )
            if not clicked_selector:
                await page.keyboard.press("Enter")
                clicked_selector = "keyboard:Enter"

        await page.wait_for_timeout(1200)
        agreed_privacy = False
        try:
            agree = page.get_by_text("同意", exact=True)
            if await agree.count() and await agree.first.is_visible(timeout=2000):
                await agree.first.click()
                agreed_privacy = True
                await page.wait_for_timeout(800)
                # The first submit opens the privacy modal; submit again after accepting.
                await click_first(page, ["input.btn-submit", "button:has-text('登录')", ".ant-btn-primary", ".el-button--primary"])
        except Exception:
            pass

        try:
            await page.wait_for_load_state("networkidle", timeout=15000)
        except PlaywrightTimeoutError:
            pass
        await page.wait_for_timeout(5000)

        if "directional-purchase" not in page.url:
            try:
                await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
                await page.wait_for_timeout(5000)
            except Exception:
                pass

        after_login = await collect_elements(page)

        # Try common actions that reveal hidden controls, without committing destructive work.
        modal_snapshots = []
        for text in ["批量导入", "上传", "导入", "新增", "查询", "重置"]:
            locator = page.get_by_text(text, exact=False)
            try:
                count = min(await locator.count(), 3)
                for i in range(count):
                    item = locator.nth(i)
                    if await item.is_visible(timeout=1000):
                        before_url = page.url
                        await item.click(timeout=3000)
                        await page.wait_for_timeout(1200)
                        modal_snapshots.append({"trigger": text, "urlBefore": before_url, "snapshot": await collect_elements(page)})
                        close = page.locator(".ant-modal-close, .el-dialog__headerbtn, button:has-text('取消'), button:has-text('关闭')").first
                        if await close.count():
                            try:
                                if await close.is_visible(timeout=1000):
                                    await close.click()
                                    await page.wait_for_timeout(500)
                            except Exception:
                                pass
                        break
            except Exception:
                continue

        try:
            await page.screenshot(path=str(SHOT), full_page=True)
        except Exception:
            pass

        result = {
            "login": {
                "usernameSelector": username_selector,
                "passwordSelector": password_selector,
                "clickedSelector": clicked_selector,
                "agreedPrivacy": agreed_privacy,
            },
            "beforeLogin": login_before,
            "afterLogin": after_login,
            "modalSnapshots": modal_snapshots,
            "requests": requests[-250:],
            "responses": responses[-250:],
            "console": console[-100:],
        }
        OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
