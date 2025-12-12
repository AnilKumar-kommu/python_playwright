
from playwright.sync_api import Page,expect


def slect_checki_in_date(page:Page,day,month,year):
    while True:
        checkin_mounth_year=page.locator(".be2db1c937").nth(0).inner_text()
        current_month,current_year=checkin_mounth_year.split(" ") #use this when the month and year in same text in locater
        if current_month== month and current_year== year:
            break
        else:
            page.locator("").click()
    all_dates=page.locator("").nth(0).locator("").all()
    for date in all_dates:
        if date.inner_text()==day:
            date.click()
            break
