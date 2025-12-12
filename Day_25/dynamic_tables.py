import pytest
from playwright.sync_api import Page,expect


def test_verify_dynamic_tabel(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

