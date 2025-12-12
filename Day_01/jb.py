from playwright.sync_api import Page, expect


def test_jb(page: Page):


    page.goto("https://mytech.justbilling.co/")

    page.locator("#AppLogin_txt_UserName_I").fill("vaazid.khan@effiasoft.com")
    page.locator("#AppLogin_txt_Password_I").fill("123456")
    page.locator("#AppLogin_ButtonLogon_CD").click()
    page.wait_for_timeout(2000)
    frams1 = page.frames
    page.frame_locator("#BIM_DashboardNew").get_by_text("SKIP", exact=True)
    page.wait_for_timeout(5000)
    frams=page.frames
    print(frams1)
    print(frams)




