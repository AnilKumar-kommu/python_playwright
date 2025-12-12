from playwright.sync_api import sync_playwright

"""
Notes:
page.wait_for_selector("text=...") ensures the text is present before you call text_content.
text_content("text=...") returns the visible text string (useful for assertions or logging).
Prefer get_by_role() for inputs/buttons; fall back to CSS/XPath where appropriate — and always assert visible text for user-facing confirmations.
"""


from playwright.sync_api import sync_playwright

def test_hover_view_details():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto("https://demo.cruisebooking.local")

        # --- Login (get_by_role) ---
        page.get_by_role("textbox", name="Email").fill("qa_user@example.com")
        page.get_by_role("textbox", name="Password").fill("SecurePass123")
        page.get_by_role("button", name="Login").click()
        page.get_by_role("heading", name="Dashboard").wait_for()

        # --- Search (CSS) ---
        page.fill("input.search-bar", "Bahamas")
        page.click("button.search-btn")
        page.wait_for_selector(".results-list")

        # --- Hover (CSS or XPath) ---
        cruise_card = page.locator("(//div[contains(@class,'cruise-card')])[1]")
        cruise_card.hover()  # mouse over the cruise card

        # After hover, hidden "View Details" button becomes visible
        view_details_button = page.locator("(//div[contains(@class,'cruise-card')])[1]//button[text()='View Details']")
        view_details_button.click()

        # --- Validate with text_content ---
        page.wait_for_selector("text=Cruise Details")
        cruise_title = page.text_content("text=Cruise Details")

        assert "Cruise Details" in cruise_title
        print("✅ Hover action successful — cruise details page opened:", cruise_title)

        browser.close()



