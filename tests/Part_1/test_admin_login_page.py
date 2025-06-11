from pages.admin_login_page import AdminLoginPage


def test_login_to_admin_panel(browser, base_url):
    admin_login_page = AdminLoginPage(browser)

    # Открытие страницы логина
    admin_login_page.open_login_page(base_url + "/administration")

    # Ввод данных и вход
    admin_login_page.login("user", "bitnami")

    # Проверка успешного логина через заголовок
    header_text = admin_login_page.get_header_text()
    assert header_text == "Dashboard", (
        f"Ожидаемый заголовок: 'Dashboard', получено: '{header_text}'"
    )
