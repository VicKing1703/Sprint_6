from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_DOWN_ORDER_LOCATOR = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/child::button"  # кнопка "Заказать" внизу экрана
    QUESTIONS_LOCATOR = By.XPATH, "//div[text()='Вопросы о важном']/parent::div"  # раздел "Вопросы о важном"
    ACCORDION_QUESTION_LOCATOR = By.XPATH, "//div[@aria-controls='accordion__panel-{}']"  # выпадающее поле с вопросами
    ACCORDION_ANSWER_LOCATOR = By.ID, "accordion__panel-{}"  # выпадающее поле с ответами
    HEADING_TEXT_LOCATOR = By.CLASS_NAME, "Home_Header__iJKdX"  # заголовок страницы "Самокат на пару дней"
    BUTTON_COOKE_ACCEPT_LOCATOR = By.XPATH, "//button[text()='да все привыкли']"  # кнопка "да все привыкли"
    BASE_LOGO_YANDEX_LOCATOR = By.XPATH, "//a[@href='//yandex.ru']"  # логотип "Яндекс" в хедере
    BASE_LOGO_SAMOKAT_LOCATOR = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"  # логотип "Самокат" в хедере
    BASE_BUTTON_ORDER_HEADER_LOCATOR = By.XPATH, "//button[@class='Button_Button__ra12g']"  # кнопка "Заказать" в хедере
