import time
from tkinter import dialog

from playwright.sync_api import Page

from PlaywrightPracties.conftest import browser_page



def test_alerts_and_popups(browser_page):
    page=browser_page
    page.goto("https://rahulshettyacademy.com/AutomationPractice")

    def handle_confirm(dialog):
        print(f"\n alert message{dialog.message}")
        assert "Hello , Are you sure you want to confirm?" in dialog.message
        dialog.accept()
        print("Alert handled successfully")
    page.once("dialog",handle_confirm)
    page.get_by_role("button", name="Confirm").click()
    page.screenshot(path="screenshots/alert message.png")
    time.sleep(5)
    print("it working")







