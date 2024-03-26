import allure
from data import Data
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestHeaderLogoClick:

    @allure.title('Тест нажатия на логотип "Самокат" в хедере страницы')
    @allure.description('Тест, что при нажатии на логотип "Самокат" в хедере страницы открывается главная страница сайта')
    def test_header_logo_samokat_click(self, driver):

        base_page = BasePage(driver)
        main_page = MainPage(driver)

        base_page.click_to_order_button_on_header()
        base_page.click_to_samokat_logo()
        assert "на пару дней" in main_page.get_heading_text()

    @allure.title('Тест нажатия на логотип "Яндекс" в хедере страницы')
    @allure.description('Тест, что при нажатии на логотип "Яндекс" в хедере страницы открывается главная страница Дзена')
    def test_header_logo_yandex_click(self, driver):

        base_page = BasePage(driver)

        base_page.click_to_yandex_logo()
        base_page.switch_tab()
        base_page.wait_loading_site()
        assert base_page.get_current_url() == Data.URL_DZEN
