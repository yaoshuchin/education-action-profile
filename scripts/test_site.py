from playwright.sync_api import sync_playwright


BASE = "http://127.0.0.1:8000"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000})

        for path in ("/index.html", "/record.html", "/photos.html", "/share.html"):
            page.goto(BASE + path, wait_until="networkidle")
            has_visual = page.locator("img").count() > 0
            if path == "/record.html":
                has_visual = page.locator(".record-section").count() == 6 and page.evaluate("getComputedStyle(document.querySelector('#education'), '::after').backgroundImage != 'none'")
            assert has_visual, path
            assert page.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth")

        page.goto(BASE + "/index.html", wait_until="networkidle")
        page.locator("button[data-size='xlarge']").click()
        assert page.locator("body").get_attribute("data-size") == "xlarge"
        page.locator("button[data-theme='blue']").click()
        assert page.locator("body").get_attribute("data-theme") == "blue"

        page.goto(BASE + "/photos.html", wait_until="networkidle")
        page.locator("button[data-filter='sport']").click()
        assert page.url.endswith("photos.html#sport")
        assert page.locator("figure[data-category='sport']:visible").count() > 0
        assert page.locator("figure[data-category='care']:visible").count() == 0

        page.set_viewport_size({"width": 390, "height": 844})
        for path in ("/index.html", "/record.html", "/photos.html", "/share.html"):
            page.goto(BASE + path, wait_until="networkidle")
            assert page.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth"), path

        browser.close()
    print("site smoke tests passed")


if __name__ == "__main__":
    main()
