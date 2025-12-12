import pytest
from playwright.sync_api import Page, expect

def test_verify_pwmethods(page:Page):

    page.goto("https://www.flipkart.com/")

    

