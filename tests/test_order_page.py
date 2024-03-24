from data import Data
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from pages.order_page import OrderPage

from pages.main_page import MainPage


class TestOrderPage(OrderPage):

    def test_order_scooter(self):

        MainPage.click_to_element(*BasePage.BUTTON_ORDER_LOCATOR)

        self.set_who_is_the_scooter_for(
            *OrderPageLocators.TITLE_WHO_IS_THE_SCOOTER_FOR_LOCATOR,
            OrderPageLocators.FIELD_NAME_LOCATOR, Data.NAME,
            OrderPageLocators.FIELD_SURNAME_LOCATOR, Data.SURNAME,
            OrderPageLocators.FIELD_ADDRESS_LOCATOR, Data.ADDRESS,
            OrderPageLocators.KEY_SUBWAY_LOCATOR,
            OrderPageLocators.FEELD_SUBWAY_LOCATOR,
            Data.METRO_STATION, OrderPageLocators.DROPDOWN_STATION_LOCATOR,
            OrderPageLocators.FIELD_PHONE_LOCATOR, Data.PHONE,
            OrderPageLocators.BUTTON_NEXT_LOCATOR
        )

        self.check_title_about_rent(*OrderPageLocators.TITLE_ABOUT_RENT_LOCATOR)

        self.set_about_rent(
            *OrderPageLocators.TITLE_ABOUT_RENT_LOCATOR,
            OrderPageLocators.FIELD_DATE_LOCATOR,
            Data.CURRENT_DATE,
            OrderPageLocators.LIST_PERIOD_LOCATOR,
            OrderPageLocators.CHECK_PERIOD_LOCATOR,
            OrderPageLocators.CHECK_COLOR_BLACK_LOCATOR,
            OrderPageLocators.FIELD_COMMENT_LOCATOR,
            Data.COMMENT,
            OrderPageLocators.BUTTON_ORDER_LOCATOR
        )

        self.check_popup_confirmation(*OrderPageLocators.POPUP_CONFIRM_LOCATOR)

        self.click_to_button(*OrderPageLocators.POPUP_BUTTON_YES_LOCATOR)

        assert self.check_order_confirmation(*OrderPageLocators.POPUP_ORDER_COMPLETE_LOCATOR) == "Заказ оформлен"
