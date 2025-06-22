from playwright.sync_api import sync_playwright

def test_accept_analytics_cookie():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.ing.pl", timeout=60000)

        page.get_by_role("button", name="Dostosuj", exact=True).click()
        page.get_by_label("Analityczne").check(force=True)
        page.get_by_role("button", name="Zaakceptuj wybrane", exact=True).click()

        cookies = context.cookies()
        analytics_cookies = [c for c in cookies if "analytics" in c["name"].lower()]
        assert analytics_cookies, "Nie znaleziono ciasteczek analitycznych!"

        browser.close()
