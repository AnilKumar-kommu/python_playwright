from playwright.sync_api import Page, expect, sync_playwright


def test_lunch_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://rescopal-qa.mariapps.com/Home/Landing")

        page.get_by_placeholder("Email address or Username").fill("systemsupport")
        page.get_by_placeholder("Password").fill("Welcome123")
        page.get_by_role("button").click()
        page.locator("#mainmenu-btn").click()

        with page.expect_popup() as page1_info:
            page.get_by_text("CRS RCY").click()
        page1 = page1_info.value

        with page.expect_popup() as page1_info:
            page.get_by_text("CRS RCY").click()
        page1 = page1_info.value

        page1.get_by_role("textbox", name="Surname").click()
        page1.get_by_role("textbox", name="Surname").fill("AK")

        page1.get_by_role("button", name="").click()

        page1.locator(".main-data > .d-flex").first.click()
        page1.get_by_role("button", name="New Booking").click()

        # Most robust, scalable, and fastest solution (one-liner per field)

        # Click the calendar icon for Start Date
        page1.locator("span.k-icon.k-i-calendar").first.click()

        # Wait for calendar popup
        page1.wait_for_selector("kendo-calendar", state="visible")

        # Click day 26

        # Open calendar
        page1.click("span.k-i-calendar")
        page1.wait_for_selector("kendo-calendar", state="visible")

        # Click month/year header
        page1.locator("kendo-calendar .k-calendar-header .k-button").first.click()
        page1.wait_for_timeout(500)

        # Click year header again to get year view
        page1.locator("kendo-calendar .k-calendar-header .k-button").first.click()
        page1.wait_for_timeout(500)

        # Select year 2026
        page1.click("kendo-calendar td:has-text('2026')")
        page1.wait_for_timeout(500)

        # Select month December
        page1.click("kendo-calendar td:has-text('Dec')")
        page1.wait_for_timeout(500)

        # Select day 15
        page1.click("kendo-calendar td:has-text('15')")

        page1.wait_for_timeout(5000)
