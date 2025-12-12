
import pytest
from playwright.sync_api import Page,expect

def test_login_data_driven(page:Page):

    page.goto("https://demowebshop.tricentis.com/login")

