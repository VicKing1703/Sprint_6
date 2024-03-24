from pages.base_page import BasePage


class OrderPage(BasePage):

    # Заполнение полей формы и нажатие на кнопку "Далее"
    def set_who_is_the_scooter_for(self, title_who_is_the_scooter_for_locator, name_locator, name,
                                   surname_locator, surname, address_locator, address,
                                   key_subway_locator, field_subway_locator, metro_station,
                                   dropdown_station_locator, phone_locator, phone, button_next_locator):
        self.find_element_with_wait(title_who_is_the_scooter_for_locator)
        self.send_keys_to_element(name_locator, name)
        self.send_keys_to_element(surname_locator, surname)
        self.send_keys_to_element(address_locator, address)
        self.click_to_element(key_subway_locator)
        self.send_keys_to_element(field_subway_locator, metro_station)
        self.click_to_element(dropdown_station_locator)
        self.send_keys_to_element(phone_locator, phone)
        self.click_to_element(button_next_locator)

    def check_title_about_rent(self, locator):
        return self.get_text_from_element(locator)

    def set_about_rent(self, title_about_rent_locator, date_locator, date,
                       list_period_locator, check_period_locator, colour_locator,
                       comment_field_locator, comment, next_button_locator):
        self.find_element_with_wait(title_about_rent_locator)
        self.send_keys_to_element(date_locator, date)
        self.click_to_element(list_period_locator)
        self.click_to_element(check_period_locator)
        self.click_to_element(colour_locator)
        self.send_keys_to_element(comment_field_locator, comment)
        self.click_to_element(next_button_locator)

    def check_popup_confirmation(self, locator):
        return self.get_text_from_element(locator)

    def click_to_button(self, locator):
        self.click_to_element(locator)

    def check_order_confirmation(self, locator):
        return self.get_text_from_element(locator)
