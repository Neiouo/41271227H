from datetime import datetime
from playwright.sync_api import sync_playwright

#HW3

# 取得當前時間並格式化為 yyyy_mm_dd 格式
now = datetime.now()
date_str = now.strftime('%Y_%m_%d')

# 使用 Playwright 開啟瀏覽器，並截圖網頁
with sync_playwright() as p:
    # 啟動瀏覽器
    browser = p.chromium.launch(headless=True )  #日常自動化使用
    page = browser.new_page()
    

    # 訪問目標網頁
    page.goto('https://osu.ppy.sh/users/7562902/osu')
    page.evaluate("document.body.style.zoom = 0.75")

    # 截圖並將檔案儲存為當前時間作為檔名
    screenshot_path = f"{date_str}.png"
    page.screenshot(path=screenshot_path)

    print(f"截圖已儲存為: {screenshot_path}")

    # 關閉瀏覽器
    browser.close()