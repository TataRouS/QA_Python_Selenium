from pages.catalog_page import CatalogPage
from utils.currency_utils import change_currency


def test_check_change_currency_in_catalog(browser, catalog_page_url, base_url):
    catalog_page = CatalogPage(browser)

    # Открытие страницы каталога и получение начальной цены
    catalog_page.open_page(catalog_page_url)
    initial_price = catalog_page.get_product_price()

    # Смена валюты через утилиту
    change_currency(browser, base_url)

    # Обновление страницы каталога и получение новой цены
    catalog_page.open_page(catalog_page_url)
    changed_price = catalog_page.get_product_price()

    print("изначальная цена", initial_price)
    print("last цена", changed_price)

    # Проверка, что цена изменилась
    assert changed_price != initial_price, (
        "Цена на товар не изменилась при смене валюты"
    )
