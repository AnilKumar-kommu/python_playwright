import pytest
from playwright.sync_api import Page, expect, Playwright

@pytest.mark.skip()
def test_browser_context(playwright:Playwright):

   browser= playwright.chromium.launch(headless=False)
   context = browser.new_context()
   page1=context.new_page()
   page2 = context.new_page()
   page3 = context.new_page()
   page1.goto("https://www.amazon.com/")
   page1.wait_for_timeout(2000)
   page2.goto("https://www.flipkart.com/")
   page2.wait_for_timeout(2000)
   page3.goto("https://www.myntra.com/")
   page3.wait_for_timeout(2000)


def test_multiple_pages(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("popup",lambda popup:popup.wait_for_load_state())
    page.locator("#PopUp").dblclick()
    page.wait_for_timeout(2000)
    all_pages=context.pages
    print("all number of pages:",len(all_pages))

    #caputuer re all url aof the pages
    for pw in all_pages:
        print("page urls:",pw.url)
        title=page.title()
        if "playwright" in title:
            pw.locator(".getStarted_Sjon").click()
            pw.wait_for_timeout(3000)
            expect(pw).to_have_title("Installation | Playwright Python")
            pw.close()
    page.wait_for_timeout(40000)
    context.close()
    browser.close()







