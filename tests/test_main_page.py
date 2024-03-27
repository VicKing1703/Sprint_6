import allure
import pytest
from pages.main_page import MainPage
from data import DataForQuestions


class TestQuestionOnPage:

    @allure.title('Тест что ответы на вопросы верены')
    @allure.description('Тест что ответы на восемь вопросов верены')
    @pytest.mark.parametrize(
        "num, expected", [
            (0, DataForQuestions.ANSWER_0),
            (1, DataForQuestions.ANSWER_1),
            (2, DataForQuestions.ANSWER_2),
            (3, DataForQuestions.ANSWER_3),
            (4, DataForQuestions.ANSWER_4),
            (5, DataForQuestions.ANSWER_5),
            (6, DataForQuestions.ANSWER_6),
            (7, DataForQuestions.ANSWER_7)
        ])
    def test_questions(self, driver, num, expected):

        main_page = MainPage(driver)
        main_page.click_to_cooke_accept()
        main_page.scroll_to_question()
        assert main_page.get_answer_text(num) == expected
