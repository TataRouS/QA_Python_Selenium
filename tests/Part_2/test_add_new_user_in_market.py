# Регистрация нового пользователя в магазине opencart

from pages.register_page import RegisterPage
import allure


@allure.title("Регистрация нового пользователя")
@allure.description("Проверяет успешную регистрацию нового пользователя через форму регистрации")
@allure.feature("Пользователи / Регистрация")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_new_user_in_market(browser, base_url):
    register_page = RegisterPage(browser)

    with allure.step("Шаг 1: Открытие страницы регистрации"):
        register_page.open_login_page(base_url + "/en-gb?route=account/register")

    with allure.step("Шаг 2: Заполнение формы регистрации новым пользователем"):
        added_new_user = register_page.add_new_user(
            "Test_Name", "Last_Name", "test_email@email.com", "12345"
        )

    with allure.step(f"Шаг 3: Проверка сообщения о успешной регистрации: '{added_new_user}'"):
        assert added_new_user == "Your Account Has Been Created!", (
            f"Ожидаемый результат: 'Your Account Has Been Created!', получено: '{added_new_user}'"
        )
