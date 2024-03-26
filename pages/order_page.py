import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    # def select_dropdown_menu_element(self, locator_menu, locator_item):
    #     self.click_to_element(locator_menu)
    #     self.scroll_to_element(locator_item)
    #     self.click_to_element(locator_item)

    @allure.step('Заполнение всех полей формы "Для кого самокат" и нажатие на кнопку "Далее"')
    def set_who_is_the_scooter_for(self,  name, surname, address, subway_station, phone):
        self.add_text_to_element(OrderPageLocators.FIELD_NAME_LOCATOR, name)
        self.add_text_to_element(OrderPageLocators.FIELD_SURNAME_LOCATOR, surname)
        self.add_text_to_element(OrderPageLocators.FIELD_ADDRESS_LOCATOR, address)
        self.click_to_element(OrderPageLocators.KEY_SUBWAY_LOCATOR)
        self.add_text_to_element(OrderPageLocators.FIELD_SUBWAY_LOCATOR, subway_station)
        self.click_to_element(OrderPageLocators.DROPDOWN_STATION_LOCATOR)
        self.add_text_to_element(OrderPageLocators.FIELD_PHONE_LOCATOR, phone)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT_LOCATOR)

    @allure.step('Проверка загрузки страницы "Оформление аренды"')
    def check_title_about_rent(self):
        return self.find_element_with_wait(OrderPageLocators.TITLE_ABOUT_RENT_LOCATOR)

    @allure.step('Заполнение полей формы "Когда привезти самокат" и нажатие на кнопку "Заказать"')
    def set_when_to_bring_scooter(self, date):
        self.add_text_to_element(OrderPageLocators.FIELD_DATE_LOCATOR, date)
        self.click_to_element(OrderPageLocators.FIELD_DATE_LOCATOR)

    @allure.step('Выбор срока аренды "Сутки"')
    def choose_period_one_day(self):
        self.click_to_element(OrderPageLocators.LIST_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.CHECK_DAY_PERIOD_LOCATOR)

    @allure.step('Выбор срока аренды "Двое суток"')
    def choose_period_two_days(self):
        self.click_to_element(OrderPageLocators.LIST_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.CHECK_TWO_DAYS_PERIOD_LOCATOR)

    @allure.step('Выбор цвета самоката "Черный жемчуг"')
    def choose_color_scooter_black(self):
        self.click_to_element(OrderPageLocators.CHECK_COLOR_BLACK_LOCATOR)

    @allure.step('Выбор цвета самоката "Серая безысходность"')
    def choose_color_scooter_grey(self):
        self.click_to_element(OrderPageLocators.CHECK_COLOR_GREY_LOCATOR)

    @allure.step('Добавление комментария к заказу')
    def add_comment_to_order(self, comment):
        self.add_text_to_element(OrderPageLocators.FIELD_COMMENT_LOCATOR, comment)

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_ORDER_LOCATOR)

    @allure.step('Проверка появление попапа подтверждения заказа')
    def check_popup_confirmation(self):
        return self.find_element_with_wait(OrderPageLocators.POPUP_CONFIRM_LOCATOR)

    @allure.step('Нажатие на кнопку "Да" в попапе подтверждения заказа')
    def click_to_yes_button(self):
        self.click_to_element(OrderPageLocators.POPUP_BUTTON_YES_LOCATOR)

    @allure.step('Проверка попапа офрмления заказа')
    def check_order_confirmation(self):
        return self.get_text_from_element(OrderPageLocators.POPUP_ORDER_COMPLETE_LOCATOR)

    @allure.step('Нажатие на кнопку "Посмотреть статус статус"')
    def click_to_check_status_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_CHECK_STATUS)
