

from playwright.sync_api import Page, expect

def test_mouse_draganddrop(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source_element =page.locator("#draggable")
    target_element =page.locator("#droppable")

    #approch 1
    # source_element.hover()
    # page.mouse.down()
    # target_element.hover()
    # page.mouse.up()
    #
    # page.wait_for_timeout(2000)

    #approch 2
    source_element.drag_to(target_element)
    page.wait_for_timeout(2000)

    #approch 3



