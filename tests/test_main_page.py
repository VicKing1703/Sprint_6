import allure
import pytest
from pages.main_page import MainPage
from data import Data


class TestQuestionOnPage:

    @allure.title('Тест что ответы на вопросы верены')
    @allure.description('Тест что ответы на восемь вопросов верены')
    @pytest.mark.parametrize(
        "num, expected", [
            (0, Data.ANSWER_0),
            (1, Data.ANSWER_1),
            (2, Data.ANSWER_2),
            (3, Data.ANSWER_3),
            (4, Data.ANSWER_4),
            (5, Data.ANSWER_5),
            (6, Data.ANSWER_6),
            (7, Data.ANSWER_7)
        ])
    def test_questions(self, driver, num, expected):

        main_page = MainPage(driver)

        main_page.scroll_to_question()
        assert main_page.get_answer_text(num) == expected
