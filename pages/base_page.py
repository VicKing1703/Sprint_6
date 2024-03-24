from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    BASE_LOGO_YANDEX_LOCATOR = By.XPATH, "//a[@href='//yandex.ru']"  # логотип "Яндекс"
    BASE_LOGO_SAMOKAT_LOCATOR = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"  # логотип "Самокат"
    BASE_BUTTON_ORDER_LOCATOR = By.XPATH, "//button[@class='Button_Button__ra12g']"  # кнопка "Заказать" вверху экрана

    def __init__(self, driver):
        self.driver = driver

    # Метод для ожидания появления элемента
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    # Метод для нажатия на элемент
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator)).click()

    # Метод для ввода текста
    def send_keys_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Метод для получения текста
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Метод для скролла до элемента
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))