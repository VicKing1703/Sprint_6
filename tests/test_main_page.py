from pages.main_page import MainPage


class TestQuestionOnPage(MainPage):

    def test_question_on_page(self):
        self.click_to_element(*self.QUESTIONS_LOCATOR)
