from selenium.webdriver.common.by import By


class OrderPageLocators:

    TITLE_LOCATOR = By.XPATH, "//div[@class='Order_Header__BZXOb']"  # заголовок страницы "Для кого самокат"
    FEELD_NAME_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"  # поле ввода "Имя"
    FEELD_SURNAME_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"  # поле ввода "Фамилия"
    FEELD_ADDRESS_LOCATOR = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # поле ввода "Адрес"
    FEELD_PHONE_LOCATOR = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"  # поле ввода "Телефон"
    KEY_SUBWAY_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']/parent::div[@class='select-search__value']"  # поле "Станция метро"
    FEELD_SUBWAY_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"  # поле ввода "Станция метро"
    DROPDOWN_STATION_LOCATOR = By.XPATH, ("//input[@placeholder='* Станция метро']/"
                                          "parent::div[@class='select-search__value']/"
                                          "following::*[contains(text(), 'Тверская')]")  # выпадающий список станций метро
    BUTTON_NEXT_LOCATOR = By.XPATH, "//div[@class='Order_NextButton__1_rCA']/child::button"  # кнопка "Далее"
