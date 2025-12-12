import pytest
from playwright.sync_api import Page,expect,Playwright

@pytest.mark.skip()
def test_multiple_pages2(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    parent = context.new_page()

    parent.goto("https://testautomationpractice.blogspot.com/")
    #register event for handle the pages
    parent.on("page", lambda page:page.wait_for_load_state())

    parent.get_by_role("button",name="New Tab").dblclick()

    all_pages=context.pages
    print("total number of pages:",len(all_pages))



def test_multiple_pages3(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    parent_page = context.new_page()
    parent_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #register the event of the handle the pages
    parent_page.on("page",lambda page:page.wait_for_load_state())
    parent_page.wait_for_load_state()

    #page.getByRole('link', { name: 'OrangeHRM, Inc' })
    parent_page.get_by_role("link",name="OrangeHRM, Inc").click()
    parent_page.wait_for_timeout(5000)

    all_pages=context.pages
    print("total number of pages:",len(all_pages))
    print ("all page urls:",all_pages[0].url)
    print("all page urls:", all_pages[1].url)
    page1=all_pages[1]
    print("page1 title:",page1)
    #
    # # now we can work on the child page
    page1.locator('body.ContactPage').click()
    page1.wait_for_timeout(5000)



