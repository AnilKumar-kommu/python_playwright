import time

def test_mouse_actions(browser_page):
    page = browser_page
    # Navigate to the target practice page
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    time.sleep(2)  # wait for page to load completely

    # Step 1: Locate the "Mouse Hover" button element by its role with name it stored as variable as mouse_hover
    mouse_hover = page.get_by_role("button", name="Mouse Hover")

    # Step 2: Perform the mouse hover action on the button
    mouse_hover.hover()
    time.sleep(2)  # small pause to allow hover content to appear

    # Step 3: Locate the hidden content that appears after hovering
    hoverContent = page.locator(".mouse-hover-content")
    time.sleep(2)

    # Step 4: Wait until the hover content becomes visible on the screen
    hoverContent.wait_for(state="visible")
    time.sleep(2)

    # Step 5: Extract and print the text shown after mouse hover
    mtext = hoverContent.inner_text()
    page.screenshot(path="screenshots/before action_hover_action.png")
    print(mtext)  # prints "Top\nReload" in console

    # Step 6: Click the "Top" link displayed under hover content
    hoverContent.get_by_text("Top").click()

    # Step 7: Take a screenshot after performing the click action
    page.screenshot(path="screenshots/after action_hover_action.png")
    time.sleep(5)  # wait before closing to observe result

    #page.screenshot(path="screenshots/hover_action.png")
