from pages.base_page import BasePage


class OrderPage(BasePage):

    # Заполнение полей формы и нажатие на кнопку "Далее"
    def set_order(self, name_locator, surname_locator,
                  address_locator, subway_locator, station_locator,
                  phone_locator, next_button_locator):
        self.find_element_with_wait(station)
        self.send_keys_to_element(name_locator, name)
        self.send_keys_to_element(surname_locator, surname)
        self.send_keys_to_element(address_locator, adress)
        self.click_to_element(subway_locator)
        self.click_to_element(station_locator)
        self.send_keys_to_element(phone_locator, phone)
        self.click_to_element(next_button_locator)

    def check_order(self, locator):
        return self.get_text_from_element(locator)
