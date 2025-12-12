
import pytest
from playwright.sync_api import Page,expect

def test_boot_strap(page:Page):

    # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # page.get_by_placeholder("Username").fill("Admin")
    # page.get_by_placeholder("Password").fill("admin123")
    # page.get_by_role("button",name="Login").click()

    page.goto("https://testautomationpractice.blogspot.com/")
    #page.locator("#datepicker").fill("22/11/2025")
    start=page.get_by_label("start-date")
    expect(start).to_be_visible()
    start.fill("21-11-2025")

    end=page.get_by_label("end-date")
    expect(end).to_be_visible()
    end.fill("30-12-2025")
    page.wait_for_timeout(5000)