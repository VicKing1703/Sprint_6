from pages.base_page import BasePage


class MainPage(BasePage):

    BUTTON_DOWN_ORDER_LOCATOR = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/child::button"  # кнопка "Заказать" внизу экрана
    QUESTIONS_LOCATOR = By.XPATH, "//div[text()='Вопросы о важном']/parent::div"  # раздел "Вопросы о важном"
    ACCORDION_QUESTION_LOCATOR = By.XPATH, "//div[@aria-controls='accordion__panel-4{}']"  # выпадающее поле с вопросами
    ACCORDION_ANSWER_LOCATOR = By.ID, "accordion__panel-4{}"  # выпадающее поле с ответами

    def click_to_element(self, locator):
        self.click_to_element(locator)

    def send_keys_to_element(self, locator, text):
        self.send_keys_to_element(locator, text)

    def get_text_from_element(self, locator):
        return self.get_text_from_element(locator)

