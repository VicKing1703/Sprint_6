from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGO_YANDEX_LOCATOR = By.XPATH, "//a[@href='//yandex.ru']"  # логотип "Яндекс"
    LOGO_SAMOKAT_LOCATOR = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"  # логотип "Самокат"
    BUTTON_ORDER_LOCATOR = By.XPATH, "//button[@class='Button_Button__ra12g']"  # кнопка "Заказать" вверху экрана
    BUTTON_DOWN_ORDER_LOCATOR = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/child::button"  # кнопка "Заказать" внизу экрана
    QUESTIONS_LOCATOR = By.XPATH, "//div[text()='Вопросы о важном']/parent::div"  # раздел "Вопросы о важном"
    ACCORDION_QUESTION_LOCATOR = By.XPATH, "//div[@aria-controls='accordion__panel-4{}']"  # выпадающее поле с вопросами
    ACCORDION_ANSWER_LOCATOR = By.ID, "accordion__panel-4{}"  # выпадающее поле с ответами
