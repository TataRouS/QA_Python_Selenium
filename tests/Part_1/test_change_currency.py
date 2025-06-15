from pages.main_page import MainPage


def test_check_change_currency_in_main_page(browser, base_url):
    main_page = MainPage(browser)

    # Открытие главной страницы
    main_page.open_main_page(base_url)

    # Получение цены товара до изменения валюты
    initial_price = main_page.get_product_price()

    # Смена валюты на Euro
    main_page.change_currency_to_euro()

    # Обновление страницы
    main_page.open_main_page(base_url)

    # Получение цены после изменения валюты
    changed_price = main_page.get_product_price()

    # Проверка, что цена изменилась
    assert changed_price != initial_price, (
        "Цена на товар не изменилась при смене валюты"
    )
