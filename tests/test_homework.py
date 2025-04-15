def test_google(browser):
    browser.get("https://google.com")
    assert "Google" in browser.title

def test_yandex(browser):
    browser.get("https://ya.ru")
    assert "Яндекс" in browser.title

def test_opencart_main(browser, base_url):
    browser.get(base_url)

    assert "Your Store" in browser.title


def test_opencart_admin(browser, base_url):
    browser.get(base_url + "/administration")

    assert "Administration" in browser.title