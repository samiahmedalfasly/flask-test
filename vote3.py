
from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=300, channel='chrome')

def run_vote(url="https://docs.google.com/forms/d/e/1FAIpQLSeZ6-aP0rMCnhEreGn8aTqQ0AispJZU_ucSm97HXrz_8j3wcg/viewform", option="محمد"):
    with sync_playwright() as p:
        browser = chromium.connect_over_ws("ws://localhost:3333/ws", headless=False, slow_mo=300,)
        # browser = p.chromium.launch(headless=False, slow_mo=300, channel='chromium')
        page = browser.new_page()
        for i in range(10000000):
            try:
                page.goto(url)
                page.get_by_label(option).click()
                submit = page.locator(".Y5sE8d").click()
            except Exception as e:
                browser.close()
        browser.close()
# run_vote()
# with sync_playwright() as p2:
#     browser2 = p2.firefox.launch()
#     print("browser2", browser2)
#     page2 = browser2.new_page()
#     print("page2", page2)
#     for i in range(10000000):
#         try:
#             page2.goto(url)
#             print("page2", page2)
#             page2.screenshot('imge{}.png'.format(i))
#             option = page2.get(option)
#             print("option", option)
#             option.click()
#             page2.get_by_role("radio", name="محمد").check()
#             # page2.get_by_role("button", name="M2UYVd").click()
#             page2.screenshot('imge{}.png'.format(i))
#         except Exception as e:
#             pass
#     browser2.close()
