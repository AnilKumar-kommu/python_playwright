import time

from playwright.sync_api import Page, expect


def test_used_locaters(page:Page):
    page.goto("https://www.demoblaze.com/")


    contact=page.get_by_role("link", name="contact")
    print(f"   hear is \n the link test of the: {contact}")