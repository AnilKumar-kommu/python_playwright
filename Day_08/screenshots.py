import time

from playwright.sync_api import sync_playwright, Page
import os

def test_booking_flow_with_screenshots_and_video():
    # Create folder structure if not exist
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("videos", exist_ok=True)

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=300)

        # Start video recording for this context
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page(Page)
        

        # Step 1: Navigate to site
        page.goto("https://rahulshettyacademy.com/client/#/auth/login")

        # Step 2: Login using get_by_role
        page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
        page.get_by_placeholder("enter your passsword").fill("Iamking@000")
        page.get_by_role("button", name="Login").click()

        page.get_by_role("button", name="Home").wait_for()
        page.screenshot(path="screenshots/01_dashboard.png")

        # Step 3: Search with CSS
        page.get_by_role("button" , name="ORDERS").click()
        time.sleep(2)
        page.screenshot(path="screenshots/02_Orders_results.png")

def test_for_mouse_hover(page: Page):
    # Step 4: Hover Example using Locators
        page.goto("https://rahulshettyacademy.com/AutomationPractice")
        time.sleep(2)
        page.get_by_role("button", name="Mouse Hover").hover()
        time.sleep(2)
        page.screenshot(path="screenshots/03_hover_mouse.png").title()

    

        # # Step 5: Click “View Details” after hover
        # view_details = page.locator("(//div[contains(@class,'cruise-card')])[1]//button[text()='View Details']")
        # view_details.click()
        #
        # # Step 6: Wait for details page & capture text
        # page.wait_for_selector("text=Cruise Details")
        # details_text = page.text_content("text=Cruise Details")
        # print("✅ Navigated to:", details_text)
        #
        # # Step 7: Take final screenshot
        # page.screenshot(path="screenshots/04_details_page.png", full_page=True)
        #
        # # Step 8: Close context (Playwright will save video automatically)
        # context.close()
        # browser.close()

        print("🎥 Video saved in 'videos/' folder")
        print("📸 Screenshots saved in 'screenshots/' folder")



