import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data


class BasePage:

    BASE_LOGO_YANDEX_LOCATOR = By.XPATH, "//a[@href='//yandex.ru']"  # логотип "Яндекс" в хедере
    BASE_LOGO_SAMOKAT_LOCATOR = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"  # логотип "Самокат" в хедере
    BASE_BUTTON_ORDER_HEADER_LOCATOR = By.XPATH, "//button[@class='Button_Button__ra12g']"  # кнопка "Заказать" в хедере

    def __init__(self, driver):
        self.driver = driver

    # Метод для ожидания появления элемента
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    # Метод для нажатия на элемент
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    # Метод для ввода текста
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Метод для получения текста
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Метод для скролла до элемента
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))

    # Метод для форматирования локатора
    def format_locators(self, locator_1, num):
        method,  locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    @allure.step('Нажать на логотип "Яндекс" в хедере')
    def click_to_yandex_logo(self):
        self.click_to_element(self.BASE_LOGO_YANDEX_LOCATOR)

    @allure.step('Нажать на логотип "Самокат" в хедере')
    def click_to_samokat_logo(self):
        self.click_to_element(self.BASE_LOGO_SAMOKAT_LOCATOR)

    @allure.step('Нажать на кнопку "Заказать" в хедере')
    def click_to_order_button_on_header(self):
        self.click_to_element(self.BASE_BUTTON_ORDER_HEADER_LOCATOR)

    @allure.step('Переключиться на новую вкладку')
    def switch_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание загрузки сайта')
    def wait_loading_site(self):
        WebDriverWait(self.driver,10).until(expected_conditions.url_to_be(Data.URL_DZEN))