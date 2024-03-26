import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    BUTTON_DOWN_ORDER_LOCATOR = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/child::button"  # кнопка "Заказать" внизу экрана
    QUESTIONS_LOCATOR = By.XPATH, "//div[text()='Вопросы о важном']/parent::div"  # раздел "Вопросы о важном"
    ACCORDION_QUESTION_LOCATOR = By.XPATH, "//div[@aria-controls='accordion__panel-{}']"  # выпадающее поле с вопросами
    ACCORDION_ANSWER_LOCATOR = By.ID, "accordion__panel-{}"  # выпадающее поле с ответами
    HEADING_TEXT_LOCATOR = By.CLASS_NAME, "Home_Header__iJKdX"  # заголовок страницы "Самокат на пару дней"

    @allure.step('Проскроллить страницу до вопросов')
    def scroll_to_question(self):
        self.scroll_to_element(self.QUESTIONS_LOCATOR)

    @allure.step('Получение текста ответа нажатием на вопрос')
    def get_answer_text(self, num):
        locator_question_format = self.format_locators(self.ACCORDION_QUESTION_LOCATOR, num)
        locator_answer_format = self.format_locators(self.ACCORDION_ANSWER_LOCATOR, num)
        self.click_to_element(locator_question_format)
        return self.get_text_from_element(locator_answer_format)

    @allure.step('Проскроллить до кнопки "Заказать" внизу экрана и нажать ее')
    def scroll_and_click_to_down_order_button(self):
        self.scroll_to_element(self.BUTTON_DOWN_ORDER_LOCATOR)
        self.click_to_element(self.BUTTON_DOWN_ORDER_LOCATOR)

    @allure.step('Получить заголовок страницы "Самокат на пару дней"')
    def get_heading_text(self):
        return self.get_text_from_element(self.HEADING_TEXT_LOCATOR)