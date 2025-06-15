from pages.catalog_page import CatalogPage


def test_check_categories(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open_page(catalog_page_url)
    assert catalog_page.check_menu_exists(), "Элемент меню не найден"


def test_check_shop_cart_of_first_product(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open_page(catalog_page_url)
    assert catalog_page.check_first_product_cart_exists(), (
        "Кнопка добавления в корзину не найдена"
    )


def test_check_menu_item(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open_page(catalog_page_url)
    catalog_page.hover_navbar_menu_item()
    assert catalog_page.get_submenu_text() == "Show All Laptops & Notebooks", (
        "Текст элемента меню не соответствует ожидаемому"
    )


def test_check_category_name(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open_page(catalog_page_url)
    assert catalog_page.get_category_name_text() == "Phones & PDAs (3)", (
        "Название категории не соответствует ожидаемому"
    )


def test_check_category_on_click_menu(browser, catalog_page_url):
    catalog_page = CatalogPage(browser)
    catalog_page.open_page(catalog_page_url)
    browser.set_window_size(800, 800)
    catalog_page.open_mobile_menu()
    browser.set_window_size(1200, 1000)
    assert catalog_page.check_mobile_category_exists(), "Мобильная категория не найдена"
