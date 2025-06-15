# Переключение валют из верхнего меню opencart
from pages.currency_top import TopPage


def test_check_change_currency_in_top(browser, base_url):
    top_page = TopPage(browser)

    # Открытие страницы логина
    top_page.open_login_page(base_url)

    previous_currency = top_page.get_previous_currency()
    actual_currency = top_page.change_currency()

    assert previous_currency != actual_currency, (
        f"Ожидаемый заголовок: 'Валюта изменилась!', с: '{previous_currency}' на: '{actual_currency}'"
    )
