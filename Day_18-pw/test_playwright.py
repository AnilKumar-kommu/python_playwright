import time

import pytest
from playwright.sync_api import Page, expect, sync_playwright


def test_browser_open():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.facebook.com")
        time.sleep(5)

def test_verify_testTitle(page:Page):
    page.goto("https://www.facebook.com")
    expect(page).to_have_title("Facebook – log in or sign up")


def test_collectAll_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.facebook.com")

        all_links = page.locator('a').all()
        print(len(all_links))
        







def test_verifyPageUrl(page:Page):
    page.goto("https://www.google.com/?zx=1763537637497&no_sw_cr=1") # passing the url
    expect(page).to_have_url("https://www.google.com/?zx=1763537637497&no_sw_cr=1") # expected url
    time.sleep(5)


