
import pytest
from playwright.sync_api import Page,expect


def test_verify_drop_down(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # #3 ways to select option from the dropdown
    #
    # #page.locator("#country").select_option(label="India")  # by select by the label most used this *** and Value also if it is available
    #
    # #selected =page.locator("#country").select_option(index=5) # by select by the index
    # selected = page.locator("#country")
    # expect(selected).to_be_visible()  # this the playwright assertion
    # selected.select_option(index=5)


    #page.locator("#colors").select_option(label=['Red'])
    #page.locator("#colors").select_option(value=['Red','white','green']) # we can select by random values by values

    total=page.locator("#colors>option")
    expect(total).not_to_have_count(9)
    page.wait_for_timeout(5000)





