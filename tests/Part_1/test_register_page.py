from pages.register_page import RegisterPage


def test_check_my_account_menu(browser, register_account_page_url):
    register_page = RegisterPage(browser)
    register_page.open_page(register_account_page_url)
    register_page.click_my_account_menu()
    assert register_page.check_login_link_exists(), (
        "Ссылка 'Login' в меню 'My Account' не найдена"
    )


def test_check_continue_button(browser, register_account_page_url):
    register_page = RegisterPage(browser)
    register_page.open_page(register_account_page_url)
    assert register_page.check_continue_button_exists(), "Кнопка Continue не найдена"


def test_check_subscribe_checkbox(browser, register_account_page_url):
    register_page = RegisterPage(browser)
    register_page.open_page(register_account_page_url)
    assert register_page.check_subscribe_checkbox_exists(), (
        "Чек-бокс подписки не найден"
    )


def test_check_email_field(browser, register_account_page_url):
    register_page = RegisterPage(browser)
    register_page.open_page(register_account_page_url)
    assert register_page.check_email_field_exists(), "Поле ввода email не найдено"


def test_check_header(browser, register_account_page_url):
    register_page = RegisterPage(browser)
    register_page.open_page(register_account_page_url)
    header_text = register_page.get_header_h1_text()
    assert header_text == "Register Account", (
        f"Ожидаемый заголовок: 'Register Account', получено: '{header_text}'"
    )
