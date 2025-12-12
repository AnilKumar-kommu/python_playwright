import time


def test_droup_downlist(browser_page):
    page = browser_page
    # Navigate to the target practice page
    page.goto("https://www.yatra.com/")
    fromList= page.locator('#input-with-icon-adornment-label')
    fromList.clear()
    fromList.type("new",delay=100)
    page.wait_for_selector("div.MuiBox-root.css-offmes")
    page.locator('div.MuiBox-root.css-offmes', has_text='new delhi').click()
    time.sleep(5)





