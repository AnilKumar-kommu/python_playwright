

from playwright.sync_api import Page,expect

def test_open_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1=page.locator("#singleFileInput").set_input_files("")
