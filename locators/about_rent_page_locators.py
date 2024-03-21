from selenium.webdriver.common.by import By


class AboutRentPageLocators:

    TITLE_LOCATOR = By.XPATH, "//div[@class='Order_Header__BZXOb']"  # заголовок страницы "Про аренду"
    FEELD_DATE_LOCATOR = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"  # поле "Когда привезти самокат"
    LIST_PERIOD_LOCATOR = By.XPATH, "//div[@class='Dropdown-control']"  # выпадающий список "Срок аренды"
    CHECK_PERIOD_LOCATOR = By.XPATH, "//*[@class='Dropdown-option'][*]"  # элемент выпадающего списка "Срок аренды"
    CHECK_COLOR_BLACK_LOCATOR = By.XPATH, "//label[@for='black']"  # чекбокс "Черный жемчуг"
    CHECK_COLOR_GREY_LOCATOR = By.XPATH, "//label[@for='grey']"  # чекбокс "Серая безысходность"
    FEELD_COMMENT_LOCATOR = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # поле "Комментарий для курьера"
    BUTTON_ORDER_LOCATOR = By.XPATH, "//div[@class='Order_Buttons__1xGrp']/child::button[text()='Заказать']"  # кнопка "Заказать"
    POPUP_CONFIRM_LOCATOR = By.NAME, "Хотите оформить заказ?"  # всплывающее окно "Хотите оформить заказ?"
    POPUP_BUTTON_YES_LOCATOR = By.XPATH, "//button[[text()='Да']"  # кнопка "Да" в всплывающем окне "Хотите оформить заказ?"
    POPUP_ORDER_COMLETE_LOCATOR = By.NAME, "Заказ оформлен"  # надпись в попапе "Заказ оформлен"
    POPUP_BUTTON_CHECK_STATUS_LOCATOR = By.NAME, "Посмотреть статус"  # кнопка "Ппосмотреть статус" в попапе "Заказ оформлен"
