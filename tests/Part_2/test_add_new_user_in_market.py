# Регистрация нового пользователя в магазине opencart

from pages.register_page import RegisterPage


def test_add_new_user_in_market(browser, base_url):
    register_page = RegisterPage(browser)

    # Открытие страницы логина
    register_page.open_login_page(base_url + "/en-gb?route=account/register")

    # Добавление нового пользователя
    added_new_user = register_page.add_new_user(
        "Test_Name", "Last_Name", "test_email@email.com", "12345"
    )

    assert added_new_user == "Your Account Has Been Created!", (
        f"Ожидаемый заголовок: 'Новый пользователь добавлен!', получено: '{added_new_user}'"
    )
