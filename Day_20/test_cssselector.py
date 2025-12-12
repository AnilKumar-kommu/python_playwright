
"""
tag id   --->tag #id
tag class  --> tag.class
tag attribute
tag class attribute

"""

import pytest
from playwright.sync_api import Page,expect


def test_verify_css_locators(page:Page):
    page.goto("https://google.com")
    page.wait_for_timeout(5000)

    # page.locator(
    #     "a[href*='https://google.com']").fill("anil")
