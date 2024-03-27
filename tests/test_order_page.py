import allure
from data import DataForForms
from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestOrderPage:

    @allure.title('Тест оформления заказа через кнопку в хедере страницы')
    @allure.description('Оформляем заказ через кнопку "Заказать" в хеддере страницы, '
                        'с заполнением только обязательных полей')
    def test_order_scooter_from_header_button(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)

        main_page.click_to_order_button_on_header()
        order_page.set_who_is_the_scooter_for(DataForForms.NAME, DataForForms.SURNAME,
                                              DataForForms.ADDRESS, DataForForms.METRO_STATION, DataForForms.PHONE)
        order_page.check_title_about_rent()
        order_page.set_when_to_bring_scooter(DataForForms.CURRENT_DATE)
        order_page.choose_period_one_day()
        order_page.click_to_order_button()
        order_page.check_popup_confirmation()
        order_page.click_to_yes_button()
        assert 'Заказ оформлен' in order_page.check_order_confirmation()

    @allure.title('Тест оформления заказа через кнопку в нижней части страницы')
    @allure.description('Оформляем заказ через кнопку "Заказать" в нижней части страницы, с заполнением всех полей')
    def test_order_scooter_from_down_button(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)

        main_page.scroll_and_click_to_down_order_button()
        order_page.set_who_is_the_scooter_for(DataForForms.NAME, DataForForms.SURNAME,
                                              DataForForms.ADDRESS, DataForForms.METRO_STATION, DataForForms.PHONE)
        order_page.check_title_about_rent()
        order_page.set_when_to_bring_scooter(DataForForms.CURRENT_DATE)
        order_page.choose_period_two_days()
        order_page.choose_color_scooter_grey()
        order_page.add_comment_to_order(DataForForms.COMMENT)
        order_page.click_to_order_button()
        order_page.check_popup_confirmation()
        order_page.click_to_yes_button()
        assert 'Заказ оформлен' in order_page.check_order_confirmation()
