from selenium.webdriver.common.by import By
from data import Data


class OrderPageLocators:

    TITLE_WHO_IS_THE_SCOOTER_FOR_LOCATOR = By.XPATH, "//div[@class='Order_Header__BZXOb']"  # заголовок страницы "Для кого самокат"
    FIELD_NAME_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"  # поле ввода "Имя"
    FIELD_SURNAME_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"  # поле ввода "Фамилия"
    FIELD_ADDRESS_LOCATOR = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # поле ввода "Адрес"
    FIELD_PHONE_LOCATOR = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"  # поле ввода "Телефон"
    KEY_SUBWAY_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']/parent::div[@class='select-search__value']"  # поле "Станция метро"
    FIELD_SUBWAY_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"  # поле ввода "Станция метро"
    DROPDOWN_STATION_LOCATOR = By.XPATH, ("//input[@placeholder='* Станция метро']/"
                                          "parent::div[@class='select-search__value']/"
                                          "following::*[contains(text(), '") + Data.METRO_STATION + "')]"  # выпадающий список станций метро (да, можно более универсальный локатор, но...
    BUTTON_NEXT_LOCATOR = By.XPATH, "//button[text()='Далее']"  # кнопка "Далее"
    TITLE_ABOUT_RENT_LOCATOR = By.XPATH, "//div[text()='Про аренду']"  # заголовок страницы "Про аренду"
    FIELD_DATE_LOCATOR = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"  # поле "Когда привезти самокат"
    DROPDOWN_TODAY_LOCATOR = By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]"  # сегодняшний день в выпадающем календаре
    LIST_PERIOD_LOCATOR = By.XPATH, "//div[@class='Dropdown-root']"  # выпадающий список "Срок аренды"
    CHECK_DAY_PERIOD_LOCATOR = By.XPATH, "//*[@class='Dropdown-option' and contains(text(), 'сутки')]"  # элемент "Сутки" выпадающего списка "Срок аренды"
    CHECK_TWO_DAYS_PERIOD_LOCATOR = By.XPATH, "//*[@class='Dropdown-option' and contains(text(), 'двое суток')]"  # элемент "двое сутки" выпадающего списка "Срок аренды"
    CHECK_COLOR_BLACK_LOCATOR = By.XPATH, "//label[@for='black']"  # чекбокс "Черный жемчуг"
    CHECK_COLOR_GREY_LOCATOR = By.XPATH, "//label[@for='grey']"  # чекбокс "Серая безысходность"
    FIELD_COMMENT_LOCATOR = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # поле "Комментарий для курьера"
    BUTTON_ORDER_LOCATOR = By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"  # кнопка "Заказать"
    POPUP_CONFIRM_LOCATOR = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"  # всплывающее окно "Хотите оформить заказ?"
    POPUP_BUTTON_YES_LOCATOR = By.XPATH, "//button[text()='Да']"  # кнопка "Да" в всплывающем окне "Хотите оформить заказ?"
    POPUP_ORDER_COMPLETE_LOCATOR = By.XPATH, "//div[text()='Заказ оформлен']"  # надпись в попапе "Заказ оформлен"
    BUTTON_CHECK_STATUS = By.XPATH, "//button[text()='Посмотреть статус']"  # кнопка "Посмотреть статус" в попапе "Заказ оформлен"

