import allure
import pytest
from pages.base_page import BasePage
from pages.home_page import HomePage
from src.data import DataInfo


class TestFAQ(BasePage):
    @pytest.mark.parametrize("question_index, expected_answer", DataInfo.FAQ_TEST_DATA)
       
    @allure.title("Проверка открытия ответов на вопросы в блоке 'Вопросы о важном'")
    @allure.description("Проверка того, что после нажатия на вопрос открывается текст ответа")

    def test_faq_answers(self, firefox_driver, question_index, expected_answer):  # Проверить, что после нажатия на вопрос откроется текст ответа.
        home_page = HomePage(firefox_driver)

        TestFAQ.scroll_down_to_bottom()  # Прокрутить в самый низ страницы

        home_page.click_faq_question(question_index)
        actual_answer = home_page.get_faq_answer_text(question_index)
        assert actual_answer == expected_answer, (f"Текст ответа на вопрос {question_index} не совпадает с ожидаемым")
