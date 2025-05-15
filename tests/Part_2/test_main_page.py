# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
# from conftest import browser
#
# # # 1 Поиск элемента Карусель вверху
# # def test_check_carousel_item(browser, base_url):
# #     browser.get(base_url)
# #     wait = WebDriverWait(browser, 5, poll_frequency=1)
# #     wait.until(method = EC.visibility_of_element_located((By.ID, "carousel-banner-0")), message = "Не появился элемент (carousel-banner-0)")
# #     carousel_item = browser.find_element(By.ID, "carousel-banner-0")
# #     assert carousel_item is not None, "Элемент не найден"
# #
# # # 2 Поиск картинки в карусели вверху
# # def test_image_from_carousel(browser, base_url):
# #     browser.get(base_url)
# #     wait = WebDriverWait(browser, 10, poll_frequency=1)
# #     carousel_item = wait.until(method=EC.visibility_of_element_located((By.XPATH, '//*[@id="carousel-banner-0"]/div[2]/div[2]/div/div')),
# #                message = "Не появился элемент (//*[@id=\"carousel-banner-0\"]/div[2]/div[2]/div/div)")
# #     assert carousel_item is not None, "Элемент не найден"
# #
# # # 3 Поиск картинки в карусели внизу
# # def test_image_starbacks_coffie (browser, base_url):
# #     browser.get(base_url)
# #     wait = WebDriverWait(browser, 15, poll_frequency=1)
# #     image_starbacks_coffie = wait.until(method=EC.visibility_of_element_located((By.XPATH, '//*[@id="carousel-banner-1"]/div[2]/div[2]/div/div[5]/img')),
# #                message = 'Не появился элемент (/*[@id="carousel-banner-1"]/div[2]/div[2]/div/div[5]/img)' )
# #     assert image_starbacks_coffie is not None, "Элемент не найден"
#
#  4 Картинка в карусели
# def test_image_from_carousel_on_click(browser, base_url):
#     browser.get(base_url)
#     wait = WebDriverWait(browser, 5, poll_frequency=1)
#     # использовать ожидания от него
#     element = wait.until(method=EC.presence_of_element_located((By.XPATH, "//*[@id=\"carousel-banner-1\"]/div[1]/button[2]")),
#         message="Не появился элемент ('//*[@id=\"carousel-banner-1\"]')")
#     browser.execute_script("arguments[0].scrollIntoView();", element)
#     time.sleep(3)
#     browser.find_element(By.XPATH, "//*[@id=\"carousel-banner-1\"]/div[1]/button[1]").click()
#     image = wait.until(method=EC.visibility_of_element_located((By.XPATH, '//*[@id="carousel-banner-1"]/div[2]/div[1]/div/div[3]/img')),
#                      message = "Не появился элемент ('//*[@id=\"carousel-banner-1\"]/div[2]/div[1]/div/div[3]/img')")
#     assert image.get_attribute("alt") == "Disney"
#
#  5 Поиск правой кнопки со стрелкой в карусели внизу
# def test_right_button_from_carousel(browser, base_url):
#     browser.get(base_url)
#     wait = WebDriverWait(browser, 10, poll_frequency=1)
#     #Наведение курсора на карусель
#     actions = ActionChains(browser)
#     element = wait.until(method=EC.presence_of_element_located((By.XPATH, "//*[@id=\"carousel-banner-1\"]/div[1]/button[2]")),
#                           message="Не появился элемент ('//*[@id=\"carousel-banner-1\"]')")
#     browser.execute_script("arguments[0].scrollIntoView();", element)
#     time.sleep(3)  # Для демонстрации
#     actions.move_to_element(element).perform()
#     #поиск элемента через ожидание
#     right_button = wait.until(method=EC.visibility_of_element_located((By.XPATH, "//*[@id=\"carousel-banner-1\"]/button[2]")),
#                message = "Не появился элемент ('//*[@id=\"carousel-banner-1\"]/button[2]')")
#     assert  right_button is not None, "Элемент не найден"
#
