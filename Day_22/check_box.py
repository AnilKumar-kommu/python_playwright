from calendar import weekday

import pytest
from playwright.sync_api import Page,expect

def test_verify_check_box(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")


    # select specific check box

    #sunday_checkbox=page.get_by_label("Sunday")



    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    checkboxes=[]
    checkboxes=[page.get_by_label(days) for day in days]
    print("total number of checkboxes:", len(checkboxes))

    # select the checkbox by passing th label info
    weekday="Friday"
    for label in days:
        if label ==weekday:
            checkbox=page.get_by_label(label)
            checkbox.check()
            expect(checkbox).to_be_visible()
            page.wait_for_timeout(5000)







