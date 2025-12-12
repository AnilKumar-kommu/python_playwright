from playwright.sync_api import sync_playwright

"""
Scenario: Validate if form fields accept and submit correct data.
✅ Key Browser Actions:
goto() – open booking page
fill() – enter passenger details
click() – submit the booking
"""


def test_guest_booking_form():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example-cruise-booking.com/guest-form")
        page.fill("#firstName", "John")
        page.fill("#lastName", "Doe")
        page.fill("#email", "john.doe@example.com")
        page.click("#submitForm")

        page.wait_for_selector("text=Booking Confirmed")
        assert "Booking Confirmed" in page.inner_text("body")

        browser.close()

"""

"""
