from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage


def test_check_container(browser, login_page_url):
    login_page = LoginPage(browser)
    login_page.open_page(login_page_url)
    assert login_page.check_container_exists(), "Элемент контейнера не найден"


def test_check_login_button(browser, login_page_url):
    login_page = LoginPage(browser)
    login_page.open_page(login_page_url)
    assert login_page.check_login_button_exists(), "Кнопка входа не найдена"


def test_check_my_account_item(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open_page(catalog_page_url)
    catalog_page.click_my_account_menu()
    assert catalog_page.get_login_menu_text() == "Login", (
        "Текст элемента меню 'Мой аккаунт' не соответствует ожидаемому"
    )


def test_check_currency(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open_page(catalog_page_url)
    catalog_page.click_currency_menu()
    assert catalog_page.get_euro_currency_text() == "€ Euro", (
        "Название валюты не соответствует ожидаемому"
    )


def test_check_category_on_click_menu(browser, login_page_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open_page(login_page_url)
    catalog_page.driver.set_window_size(800, 800)
    catalog_page.open_mobile_menu()
    assert catalog_page.check_mobile_category_exists(), "Мобильная категория не найдена"
